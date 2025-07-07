"""
Stock data API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from datetime import datetime, timedelta

from services.stock_service import StockService
from models.stock import StockData, StockResponse
from core.database import get_async_session

router = APIRouter()
stock_service = StockService()

@router.get("/search")
async def search_stocks(
    query: str,
    limit: int = 10
):
    """Search for stocks by symbol or company name"""
    try:
        results = await stock_service.search_stocks(query, limit)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/data")
async def get_stock_data(
    symbol: str,
    period: str = "1y",
    interval: str = "1d"
):
    """Get stock price data"""
    try:
        data = await stock_service.get_stock_data(symbol, period, interval)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/indicators")
async def get_technical_indicators(
    symbol: str,
    period: str = "1y"
):
    """Get technical indicators for a stock"""
    try:
        indicators = await stock_service.get_technical_indicators(symbol, period)
        return indicators
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))