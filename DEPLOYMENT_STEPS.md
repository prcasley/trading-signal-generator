# 🚀 EXACT DEPLOYMENT STEPS FOR PRCASLEY

## ✅ Step 1: Create GitHub Repository

**1.1 Go to GitHub:**
- Visit: https://github.com/new
- Repository name: `trading-signal-generator`
- Description: `Modern web platform for real-time trading signal generation`
- Set to **Public**
- **Don't** check "Add a README file" (we already have files)
- Click "Create repository"

**1.2 Push Your Code:**
After creating the repository, GitHub will show you commands. Since we've already prepared everything, you just need to run:

```bash
# We've already done this:
# git remote add origin https://github.com/prcasley/trading-signal-generator.git

# Push your code (you'll need to authenticate)
git push -u origin main
```

**Authentication Options:**
- Use GitHub Desktop app (easiest)
- Use personal access token
- Use SSH key

## 🖥️ Step 2: Deploy Backend to Railway

**2.1 Go to Railway:**
- Visit: https://railway.app
- Click "Login" → "Login with GitHub"
- Authorize Railway to access your GitHub

**2.2 Create New Project:**
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose `prcasley/trading-signal-generator`
- **Important:** Set root directory to `backend` (not the main folder)

**2.3 Add Environment Variables:**
In Railway dashboard, go to "Variables" tab and add:
```
ALPHA_VANTAGE_API_KEY=demo
SECRET_KEY=trading-signal-secret-key-123456789
ALLOWED_ORIGINS=https://your-app.vercel.app,http://localhost:3000
PORT=8000
```

**2.4 Deploy:**
- Railway will automatically build and deploy
- Copy your Railway URL (e.g., `https://trading-signal-backend-production.railway.app`)
- Test it: Visit `YOUR_RAILWAY_URL/health`

## 🌐 Step 3: Deploy Frontend to Vercel

**3.1 Go to Vercel:**
- Visit: https://vercel.com
- Click "Sign Up" → "Continue with GitHub"
- Authorize Vercel

**3.2 Import Project:**
- Click "New Project"
- Import `prcasley/trading-signal-generator`
- **Important:** Set root directory to `frontend`
- Framework: Create React App (auto-detected)

**3.3 Add Environment Variables:**
In Vercel dashboard, go to "Settings" → "Environment Variables":
```
REACT_APP_API_URL=YOUR_RAILWAY_URL_HERE
REACT_APP_WS_URL=wss://YOUR_RAILWAY_URL_WITHOUT_HTTPS/ws
```

Example:
```
REACT_APP_API_URL=https://trading-signal-backend-production.railway.app
REACT_APP_WS_URL=wss://trading-signal-backend-production.railway.app/ws
```

**3.4 Deploy:**
- Click "Deploy"
- Vercel will build and deploy
- Copy your Vercel URL (e.g., `https://trading-signal-generator.vercel.app`)

## 🔧 Step 4: Final Configuration

**4.1 Update CORS in Railway:**
- Go back to Railway dashboard
- Update `ALLOWED_ORIGINS` variable:
```
ALLOWED_ORIGINS=https://YOUR_ACTUAL_VERCEL_URL.vercel.app,http://localhost:3000
```

**4.2 Test Everything:**
- Backend health: `YOUR_RAILWAY_URL/health`
- Frontend: `YOUR_VERCEL_URL`
- Signals API: `YOUR_RAILWAY_URL/api/v1/signals`

## 🎯 URLs You'll Get:

**Backend (Railway):** 
- Format: `https://trading-signal-backend-production.railway.app`
- Health check: Add `/health` to the end

**Frontend (Vercel):**
- Format: `https://trading-signal-generator.vercel.app`
- Full trading dashboard

## 🚨 If You Get Stuck:

**GitHub Push Issues:**
- Use GitHub Desktop app for easier authentication
- Or create Personal Access Token in GitHub settings

**Railway Issues:**
- Make sure root directory is set to `backend`
- Check build logs in Railway dashboard

**Vercel Issues:**
- Make sure root directory is set to `frontend`
- Check environment variables are correct

## ✅ Success Indicators:

1. **GitHub:** Code visible at `https://github.com/prcasley/trading-signal-generator`
2. **Railway:** Backend API responds at `/health` endpoint
3. **Vercel:** Frontend loads with trading dashboard
4. **Integration:** Frontend shows live trading signals from backend

---

**Ready to start? Begin with Step 1: Create the GitHub repository!**