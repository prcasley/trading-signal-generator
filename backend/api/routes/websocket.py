"""
WebSocket API endpoints
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def websocket_status():
    """Get WebSocket connection status"""
    return {"status": "available", "endpoint": "/ws/{client_id}"}