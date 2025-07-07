"""
Signal data models
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class Signal(BaseModel):
    id: Optional[int] = None
    symbol: str
    signal_type: str  # BUY, SELL, HOLD
    confidence: float
    price: float
    timestamp: datetime
    indicators: Optional[Dict[str, Any]] = None
    reasoning: Optional[str] = None

class SignalResponse(BaseModel):
    id: int
    symbol: str
    signal_type: str
    confidence: float
    price: float
    timestamp: datetime
    indicators: Optional[Dict[str, Any]] = None
    reasoning: Optional[str] = None
    change: Optional[str] = None