"""
FastAPI Backend for Trading Signal Generator
Modern, scalable backend with real-time WebSocket support
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncio
import json
from typing import Dict, List, Optional
from datetime import datetime
import logging

from api.routes import signals, stocks, websocket
from core.config import settings
from core.database import init_db
from services.signal_service import SignalService
from services.websocket_manager import WebSocketManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Trading Signal Generator API",
    description="Modern, scalable trading signal generation platform",
    version="2.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
signal_service = SignalService()
websocket_manager = WebSocketManager()

# Include API routes
app.include_router(signals.router, prefix="/api/v1/signals", tags=["signals"])
app.include_router(stocks.router, prefix="/api/v1/stocks", tags=["stocks"])
app.include_router(websocket.router, prefix="/api/v1/websocket", tags=["websocket"])

@app.on_event("startup")
async def startup_event():
    """Initialize database and services on startup"""
    try:
        await init_db()
        logger.info("Database initialized successfully")
        
        # Start background tasks
        asyncio.create_task(real_time_signal_generator())
        logger.info("Real-time signal generator started")
        
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    await websocket_manager.disconnect_all()
    logger.info("Application shutdown complete")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/")
async def root():
    """Root endpoint with API info"""
    return {
        "message": "Trading Signal Generator API",
        "version": "2.0.0",
        "docs": "/api/docs",
        "health": "/health"
    }

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """WebSocket endpoint for real-time updates"""
    await websocket_manager.connect(websocket, client_id)
    
    try:
        while True:
            # Keep connection alive and handle incoming messages
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Handle different message types
            if message.get("type") == "subscribe":
                symbol = message.get("symbol")
                if symbol:
                    await websocket_manager.subscribe_to_symbol(client_id, symbol)
                    await websocket.send_text(json.dumps({
                        "type": "subscribed",
                        "symbol": symbol,
                        "timestamp": datetime.now().isoformat()
                    }))
            
            elif message.get("type") == "unsubscribe":
                symbol = message.get("symbol")
                if symbol:
                    await websocket_manager.unsubscribe_from_symbol(client_id, symbol)
                    await websocket.send_text(json.dumps({
                        "type": "unsubscribed", 
                        "symbol": symbol,
                        "timestamp": datetime.now().isoformat()
                    }))
                    
    except WebSocketDisconnect:
        websocket_manager.disconnect(client_id)
        logger.info(f"Client {client_id} disconnected")
    except Exception as e:
        logger.error(f"WebSocket error for client {client_id}: {e}")
        websocket_manager.disconnect(client_id)

async def real_time_signal_generator():
    """Background task for generating real-time signals"""
    while True:
        try:
            # Get active symbols from connected clients
            active_symbols = websocket_manager.get_active_symbols()
            
            for symbol in active_symbols:
                # Generate signals for active symbols
                signals = await signal_service.generate_real_time_signals(symbol)
                
                if signals:
                    # Broadcast to subscribed clients
                    await websocket_manager.broadcast_to_symbol(symbol, {
                        "type": "signal_update",
                        "symbol": symbol,
                        "signals": signals,
                        "timestamp": datetime.now().isoformat()
                    })
            
            # Wait before next update (configurable)
            await asyncio.sleep(settings.SIGNAL_UPDATE_INTERVAL)
            
        except Exception as e:
            logger.error(f"Error in real-time signal generator: {e}")
            await asyncio.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)