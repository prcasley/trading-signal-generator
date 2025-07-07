"""
WebSocket connection manager
"""
import json
from typing import Dict, Set, List
from fastapi import WebSocket
import asyncio
import logging

logger = logging.getLogger(__name__)

class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.subscriptions: Dict[str, Set[str]] = {}  # client_id -> set of symbols
        self.symbol_subscribers: Dict[str, Set[str]] = {}  # symbol -> set of client_ids
    
    async def connect(self, websocket: WebSocket, client_id: str):
        """Connect a new WebSocket client"""
        await websocket.accept()
        self.active_connections[client_id] = websocket
        self.subscriptions[client_id] = set()
        logger.info(f"Client {client_id} connected")
    
    def disconnect(self, client_id: str):
        """Disconnect a WebSocket client"""
        if client_id in self.active_connections:
            # Remove from all symbol subscriptions
            for symbol in self.subscriptions.get(client_id, set()):
                if symbol in self.symbol_subscribers:
                    self.symbol_subscribers[symbol].discard(client_id)
                    if not self.symbol_subscribers[symbol]:
                        del self.symbol_subscribers[symbol]
            
            # Remove client
            del self.active_connections[client_id]
            if client_id in self.subscriptions:
                del self.subscriptions[client_id]
            
            logger.info(f"Client {client_id} disconnected")
    
    async def disconnect_all(self):
        """Disconnect all clients"""
        for client_id in list(self.active_connections.keys()):
            self.disconnect(client_id)
    
    async def subscribe_to_symbol(self, client_id: str, symbol: str):
        """Subscribe client to a symbol"""
        if client_id in self.subscriptions:
            self.subscriptions[client_id].add(symbol)
            
            if symbol not in self.symbol_subscribers:
                self.symbol_subscribers[symbol] = set()
            self.symbol_subscribers[symbol].add(client_id)
            
            logger.info(f"Client {client_id} subscribed to {symbol}")
    
    async def unsubscribe_from_symbol(self, client_id: str, symbol: str):
        """Unsubscribe client from a symbol"""
        if client_id in self.subscriptions:
            self.subscriptions[client_id].discard(symbol)
            
            if symbol in self.symbol_subscribers:
                self.symbol_subscribers[symbol].discard(client_id)
                if not self.symbol_subscribers[symbol]:
                    del self.symbol_subscribers[symbol]
            
            logger.info(f"Client {client_id} unsubscribed from {symbol}")
    
    async def send_to_client(self, client_id: str, message: dict):
        """Send message to a specific client"""
        if client_id in self.active_connections:
            try:
                await self.active_connections[client_id].send_text(json.dumps(message))
            except Exception as e:
                logger.error(f"Error sending message to client {client_id}: {e}")
                self.disconnect(client_id)
    
    async def broadcast_to_symbol(self, symbol: str, message: dict):
        """Broadcast message to all clients subscribed to a symbol"""
        if symbol in self.symbol_subscribers:
            disconnected_clients = []
            
            for client_id in self.symbol_subscribers[symbol]:
                try:
                    await self.send_to_client(client_id, message)
                except Exception as e:
                    logger.error(f"Error broadcasting to client {client_id}: {e}")
                    disconnected_clients.append(client_id)
            
            # Remove disconnected clients
            for client_id in disconnected_clients:
                self.disconnect(client_id)
    
    def get_active_symbols(self) -> List[str]:
        """Get list of symbols that have active subscribers"""
        return list(self.symbol_subscribers.keys())
    
    def get_connection_count(self) -> int:
        """Get number of active connections"""
        return len(self.active_connections)