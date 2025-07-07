"""
Trading signals API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from datetime import datetime, timedelta
import asyncio

from services.signal_service import SignalService
from models.signal import Signal, SignalResponse
from core.database import get_async_session

router = APIRouter()
signal_service = SignalService()

@router.get("/", response_model=List[SignalResponse])
async def get_signals(
    symbol: str,
    limit: int = 50,
    session = Depends(get_async_session)
):
    """Get trading signals for a symbol"""
    try:
        signals = await signal_service.get_signals(symbol, limit)
        return signals
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
async def generate_signal(
    symbol: str,
    session = Depends(get_async_session)
):
    """Generate new trading signal for a symbol"""
    try:
        signal = await signal_service.generate_signal(symbol)
        return {"message": "Signal generated successfully", "signal": signal}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/latest")
async def get_latest_signal(
    symbol: str,
    session = Depends(get_async_session)
):
    """Get latest signal for a symbol"""
    try:
        signal = await signal_service.get_latest_signal(symbol)
        if not signal:
            raise HTTPException(status_code=404, detail="No signals found for this symbol")
        return signal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))