"""
Stock data service
"""
import asyncio
from typing import List, Dict
import yfinance as yf
import pandas as pd

class StockService:
    def __init__(self):
        pass
    
    async def search_stocks(self, query: str, limit: int = 10) -> List[Dict]:
        """Search for stocks by symbol or company name"""
        # Mock search results
        stocks = [
            {"symbol": "AAPL", "name": "Apple Inc.", "price": 150.25, "change": "+1.2%"},
            {"symbol": "GOOGL", "name": "Alphabet Inc.", "price": 2800.50, "change": "-0.5%"},
            {"symbol": "MSFT", "name": "Microsoft Corporation", "price": 280.75, "change": "+0.8%"},
            {"symbol": "TSLA", "name": "Tesla, Inc.", "price": 220.30, "change": "+2.1%"},
            {"symbol": "AMZN", "name": "Amazon.com, Inc.", "price": 3200.15, "change": "-0.3%"},
        ]
        
        # Filter by query
        filtered = [s for s in stocks if query.upper() in s["symbol"] or query.lower() in s["name"].lower()]
        return filtered[:limit]
    
    async def get_stock_data(self, symbol: str, period: str = "1y", interval: str = "1d") -> Dict:
        """Get stock price data"""
        try:
            # Use yfinance to get real data
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period, interval=interval)
            
            # Convert to JSON-serializable format
            return {
                "symbol": symbol,
                "data": data.reset_index().to_dict('records'),
                "period": period,
                "interval": interval
            }
        except Exception as e:
            # Return mock data if real data fails
            return {
                "symbol": symbol,
                "data": self._generate_mock_data(),
                "period": period,
                "interval": interval
            }
    
    async def get_technical_indicators(self, symbol: str, period: str = "1y") -> Dict:
        """Get technical indicators for a stock"""
        # Mock technical indicators
        return {
            "symbol": symbol,
            "indicators": {
                "rsi": 45.2,
                "macd": {
                    "macd": 1.25,
                    "signal": 1.18,
                    "histogram": 0.07
                },
                "bollinger_bands": {
                    "upper": 155.30,
                    "middle": 150.25,
                    "lower": 145.20
                },
                "moving_averages": {
                    "sma_20": 148.50,
                    "sma_50": 145.75,
                    "sma_200": 140.25
                }
            }
        }
    
    def _generate_mock_data(self) -> List[Dict]:
        """Generate mock stock data"""
        import random
        from datetime import datetime, timedelta
        
        data = []
        base_price = 150.0
        
        for i in range(100):
            date = datetime.now() - timedelta(days=i)
            price_change = random.uniform(-2, 2)
            base_price += price_change
            
            data.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Open": round(base_price - random.uniform(0, 1), 2),
                "High": round(base_price + random.uniform(0, 2), 2),
                "Low": round(base_price - random.uniform(0, 2), 2),
                "Close": round(base_price, 2),
                "Volume": random.randint(1000000, 10000000)
            })
        
        return list(reversed(data))