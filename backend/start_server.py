#!/usr/bin/env python3
"""
Start the trading signal server on an available port
"""

import subprocess
import socket
import sys
import os

def find_free_port(start_port=8000):
    """Find a free port starting from start_port"""
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except socket.error:
            continue
    return None

def main():
    # Find free port
    port = find_free_port(8001)
    if not port:
        print("❌ No free ports available")
        sys.exit(1)
    
    print(f"🚀 Starting Trading Signal API on port {port}")
    
    # Modify the simple_server.py to use the free port
    server_code = f'''#!/usr/bin/env python3
"""
Simple HTTP server for testing the trading signal API
Uses only built-in Python modules
"""

import http.server
import socketserver
import json
import urllib.parse
from datetime import datetime
import random

class TradingSignalHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Add CORS headers
        self.send_cors_headers()
        
        if path == '/health':
            self.handle_health()
        elif path == '/':
            self.handle_root()
        elif path.startswith('/api/v1/signals'):
            self.handle_signals()
        elif path.startswith('/api/v1/stocks'):
            self.handle_stocks()
        else:
            self.send_404()
    
    def do_OPTIONS(self):
        """Handle preflight requests"""
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()
    
    def send_cors_headers(self):
        """Send CORS headers"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def handle_health(self):
        """Health check endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {{
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "message": "Trading Signal Generator API is running",
            "port": {port}
        }}
        self.wfile.write(json.dumps(response).encode())
    
    def handle_root(self):
        """Root endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {{
            "message": "Trading Signal Generator API v2.0",
            "port": {port},
            "endpoints": {{
                "health": "/health",
                "signals": "/api/v1/signals",
                "stocks": "/api/v1/stocks",
                "docs": "API Documentation - Coming Soon"
            }},
            "status": "operational"
        }}
        self.wfile.write(json.dumps(response).encode())
    
    def handle_signals(self):
        """Handle signals endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Generate mock signals
        signals = []
        symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'NVDA', 'META']
        
        for i, symbol in enumerate(symbols):
            signal_type = random.choice(['BUY', 'SELL', 'HOLD'])
            confidence = round(random.uniform(60, 95), 1)
            price = round(random.uniform(100, 300), 2)
            change_percent = round(random.uniform(-3, 3), 2)
            
            signals.append({{
                "id": i + 1,
                "symbol": symbol,
                "signal_type": signal_type,
                "confidence": confidence,
                "price": f"${price}",
                "change": f"{{'+' if change_percent >= 0 else ''}}{change_percent}%",
                "timestamp": datetime.now().isoformat(),
                "indicators": {{
                    "rsi": round(random.uniform(20, 80), 1),
                    "macd": round(random.uniform(-2, 2), 3),
                    "volume": random.randint(1000000, 10000000)
                }}
            }})
        
        self.wfile.write(json.dumps(signals).encode())
    
    def handle_stocks(self):
        """Handle stocks search endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Mock stock search results
        stocks = [
            {{"symbol": "AAPL", "name": "Apple Inc.", "price": "$150.25", "change": "+1.2%"}},
            {{"symbol": "GOOGL", "name": "Alphabet Inc.", "price": "$2800.50", "change": "-0.5%"}},
            {{"symbol": "MSFT", "name": "Microsoft Corporation", "price": "$280.75", "change": "+0.8%"}},
            {{"symbol": "TSLA", "name": "Tesla, Inc.", "price": "$220.30", "change": "+2.1%"}},
            {{"symbol": "AMZN", "name": "Amazon.com, Inc.", "price": "$3200.15", "change": "-0.3%"}},
            {{"symbol": "NVDA", "name": "NVIDIA Corporation", "price": "$450.80", "change": "+3.2%"}},
            {{"symbol": "META", "name": "Meta Platforms, Inc.", "price": "$320.45", "change": "+1.8%"}},
        ]
        
        self.wfile.write(json.dumps(stocks).encode())
    
    def send_404(self):
        """Send 404 response"""
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {{"error": "Endpoint not found", "path": self.path}}
        self.wfile.write(json.dumps(response).encode())

def run_server(port={port}):
    """Run the server"""
    try:
        with socketserver.TCPServer(("", port), TradingSignalHandler) as httpd:
            print(f"🚀 Trading Signal API Server starting...")
            print(f"📡 Server running at http://localhost:{{port}}")
            print(f"🏥 Health check: http://localhost:{{port}}/health")
            print(f"📊 Signals API: http://localhost:{{port}}/api/v1/signals")
            print(f"🔍 Stocks API: http://localhost:{{port}}/api/v1/stocks")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {{e}}")

if __name__ == "__main__":
    run_server()
'''
    
    # Write the server file
    with open('server_port.py', 'w') as f:
        f.write(server_code)
    
    # Start the server
    print(f"📡 Backend API will be available at: http://localhost:{port}")
    print(f"🏥 Health check: http://localhost:{port}/health")
    print(f"📊 Signals: http://localhost:{port}/api/v1/signals")
    print("-" * 50)
    
    subprocess.run([sys.executable, 'server_port.py'])

if __name__ == "__main__":
    main()