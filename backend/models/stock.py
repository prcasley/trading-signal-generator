"""
Stock data models
"""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class StockData(BaseModel):
    symbol: str
    name: str
    price: float
    change: str
    volume: Optional[int] = None
    market_cap: Optional[float] = None

class StockResponse(BaseModel):
    symbol: str
    data: List[Dict[str, Any]]
    period: str
    interval: str
    indicators: Optional[Dict[str, Any]] = None