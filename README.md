# Trading Signal Generator - Web Platform

Modern, scalable web application for real-time trading signal generation with professional UI and cloud deployment.

## 🚀 Live Demo

- **Frontend**: [https://trading-signals.vercel.app](https://trading-signals.vercel.app) *(will be available after deployment)*
- **Backend API**: [https://trading-signals-api.railway.app](https://trading-signals-api.railway.app) *(will be available after deployment)*

## ⚡ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd web-platform
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Or run manually**
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload

   # Frontend  
   cd frontend
   npm install
   npm start
   ```

## ☁️ Deployment

### Vercel (Frontend)

1. **Connect to Vercel**
   ```bash
   npm install -g vercel
   cd frontend
   vercel
   ```

2. **Set environment variables in Vercel dashboard**
   - `REACT_APP_API_URL`: Your Railway backend URL
   - `REACT_APP_WS_URL`: Your Railway WebSocket URL

### Railway (Backend)

1. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Select the `backend` folder as root

2. **Add environment variables**
   - `DATABASE_URL`: PostgreSQL connection string
   - `REDIS_URL`: Redis connection string
   - `ALPHA_VANTAGE_API_KEY`: Your API key
   - `SECRET_KEY`: Random secret key
   - `ALLOWED_ORIGINS`: Your Vercel frontend URL

## 🏗️ Architecture

- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: FastAPI + WebSocket + PostgreSQL + Redis
- **Deployment**: Vercel + Railway
- **Real-time**: WebSocket connections for live updates

## 📊 Features

- ✅ Real-time trading signals
- ✅ Modern, responsive UI
- ✅ Dark/Light theme
- ✅ Stock search functionality
- ✅ WebSocket live updates
- ✅ Professional dashboard
- ✅ Mobile-friendly design
- ✅ Multi-user ready

## 🛠️ Tech Stack

### Frontend
- React 18 with TypeScript
- Tailwind CSS for styling
- React Query for API management
- Socket.io for real-time updates
- Framer Motion for animations

### Backend
- FastAPI with async support
- PostgreSQL database
- Redis for caching
- WebSocket for real-time data
- Pydantic for data validation

## 📈 Monetization Ready

This platform is designed for commercial use with:
- Multi-user architecture
- Subscription billing ready
- API rate limiting
- Professional UI/UX
- Scalable infrastructure

## 🔐 Security

- CORS protection
- Environment variable management
- SQL injection prevention
- XSS protection headers
- Secure WebSocket connections

## 📱 Mobile Support

The platform is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile phones
- Progressive Web App ready

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting guide
- Review the API documentation

---

**Built with ❤️ for professional traders and developers**