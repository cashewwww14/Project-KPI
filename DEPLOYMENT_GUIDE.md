# 🚀 Complete Deployment Guide - 5G & 4G KPI Dashboard

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Overview](#project-overview)
3. [Database Setup](#database-setup)
4. [Backend Deployment (Render)](#backend-deployment-render)
5. [Frontend Deployment (Netlify)](#frontend-deployment-netlify)
6. [Testing](#testing)
7. [Troubleshooting](#troubleshooting)
8. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Prerequisites

### Accounts Needed (All Free)
- ✅ GitHub account
- ✅ Render.com account
- ✅ Netlify account

### Tools Required
- ✅ Git installed
- ✅ Text editor (VS Code recommended)
- ✅ Database server with PostgreSQL

### Database Requirements
Your database server must:
- ✅ Be accessible from internet (public IP or ngrok)
- ✅ Have PostgreSQL running
- ✅ Allow remote connections
- ✅ Have existing KPI data tables

---

## Project Overview

### Architecture
```
Database Server (Your Server)
    ↓
Backend API (Render.com - Free)
    ↓
Frontend Dashboard (Netlify - Free)
    ├── dashboard.html (5G KPI)
    └── dashboard_4g.html (4G KPI)
```

### Tech Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Chart.js)
- **Hosting**: Render (Backend) + Netlify (Frontend)

---

## Database Setup

### Step 1: Verify Database Accessibility

#### Option A: Using Public IP (Recommended)
Your database server should have a public IP address.

**Test connection:**
```bash
psql -h YOUR_SERVER_IP -p 5432 -U postgres -d postgres
```

#### Option B: Using ngrok (Temporary)
If database is on local machine:

1. Install ngrok: https://ngrok.com/download
2. Start ngrok:
   ```bash
   ngrok tcp 5432
   ```
3. Note the forwarding address: `tcp://1.tcp.ap.ngrok.io:21039`

**⚠️ Warning**: ngrok free tier URL changes on restart!

### Step 2: Configure PostgreSQL for Remote Access

#### Edit `postgresql.conf`
```conf
listen_addresses = '*'
port = 5432
max_connections = 100
```

#### Edit `pg_hba.conf`
```conf
# Allow remote connections (use specific IP for security)
host    all    postgres    0.0.0.0/0    md5
```

#### Restart PostgreSQL
**Windows:**
```powershell
Restart-Service postgresql-x64-14
```

**Linux:**
```bash
sudo systemctl restart postgresql
```

### Step 3: Test Connection

```powershell
# Replace with your actual credentials
psql -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres
```

Should see:
```
postgres=#
```

### Step 4: Verify Tables Exist

```sql
-- Check 5G tables
SELECT COUNT(*) FROM cluster_5g;

-- Check 4G tables
SELECT COUNT(*) FROM cluster_4g;

-- List all tables
\dt
```

---

## Backend Deployment (Render)

### Step 1: Prepare Local Repository

#### 1.1 Navigate to project folder
```powershell
cd C:\Users\lenov\Documents\project\Project-KPI
```

#### 1.2 Initialize Git (if not already)
```powershell
git init
git branch -M main
```

#### 1.3 Verify required files exist
```powershell
dir
```

Should see:
- ✅ `dashboard_backend.py`
- ✅ `requirements_dashboard.txt`
- ✅ `runtime.txt`
- ✅ `Procfile`
- ✅ `.gitignore`

### Step 2: Push to GitHub

#### 2.1 Create new repository on GitHub
1. Go to https://github.com/new
2. Repository name: `kpi-dashboard`
3. Set to **Public**
4. ❌ Don't initialize with README
5. Click "Create repository"

#### 2.2 Push code to GitHub
```powershell
# Add remote
git remote add origin https://github.com/cashewwww14/kpi-dashboard.git

# Add all files
git add .

# Commit
git commit -m "Initial commit: 5G & 4G KPI Dashboard"

# Push
git push -u origin main
```

**Troubleshooting**: If asked for credentials:
- Use Personal Access Token instead of password
- Generate at: https://github.com/settings/tokens

### Step 3: Deploy on Render

#### 3.1 Create Web Service
1. Login to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect GitHub"**
4. Select repository: `kpi-dashboard`

#### 3.2 Configure Build Settings
```
Name: kpi-dashboard-backend
Region: Singapore (or closest to your location)
Branch: main
Root Directory: (leave empty)
Runtime: Python 3

Build Command:
pip install -r requirements_dashboard.txt

Start Command:
gunicorn dashboard_backend:app --bind 0.0.0.0:$PORT

Instance Type: Free
```

#### 3.3 Add Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**

**⚠️ IMPORTANT**: Replace with YOUR database credentials!

```
DB_HOST=1.tcp.ap.ngrok.io
DB_PORT=21039
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=option88
PORT=10000
```

**For Production Database** (if using public IP):
```
DB_HOST=103.xxx.xxx.xxx
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_secure_password
PORT=10000
```

#### 3.4 Create Web Service
1. Review settings
2. Click **"Create Web Service"**
3. Wait 5-10 minutes for deployment

#### 3.5 Note Your Backend URL
After deployment, you'll get:
```
https://kpi-dashboard-backend.onrender.com
```

**📝 SAVE THIS URL!** You'll need it for frontend.

### Step 4: Test Backend API

#### Test in browser:
Visit:
```
https://kpi-dashboard-backend.onrender.com/
```

Should see:
```json
{"message":"5G KPI Dashboard API","status":"running"}
```

#### Test endpoints:
```
https://kpi-dashboard-backend.onrender.com/api/nc-list
https://kpi-dashboard-backend.onrender.com/api/availability?nc=All
```

#### Test with PowerShell:
```powershell
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/api/nc-list" | Select-Object Content
```

---

## Frontend Deployment (Netlify)

### Step 1: Update Frontend Configuration

#### 1.1 Update `dashboard.html`
Find line 367 (search for `API_BASE_URL`):

**BEFORE:**
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

**AFTER:**
```javascript
// Replace with YOUR backend URL from Render
const API_BASE_URL = 'https://kpi-dashboard-backend.onrender.com/api';
```

#### 1.2 Update `dashboard_4g.html`
Find line 352 (search for `API_BASE_URL`):

**BEFORE:**
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

**AFTER:**
```javascript
// Replace with YOUR backend URL from Render
const API_BASE_URL = 'https://kpi-dashboard-backend.onrender.com/api';
```

**⚠️ CRITICAL**: Replace `kpi-dashboard-backend.onrender.com` with YOUR actual backend URL!

### Step 2: Commit Changes

```powershell
git add dashboard.html dashboard_4g.html
git commit -m "Update API URL for production"
git push origin main
```

### Step 3: Deploy on Netlify

#### Method A: Drag & Drop (Easiest)

1. Login to https://app.netlify.com
2. Click **"Add new site"** → **"Deploy manually"**
3. Drag & drop these 2 files:
   - `dashboard.html`
   - `dashboard_4g.html`
4. Wait for upload (~30 seconds)
5. Done! You'll get URL like: `https://random-name-123.netlify.app`

#### Method B: Connect GitHub (Recommended)

1. Login to https://app.netlify.com
2. Click **"Add new site"** → **"Import an existing project"**
3. Click **"Deploy with GitHub"**
4. Authorize Netlify access
5. Select repository: `kpi-dashboard`
6. Configure:
   ```
   Branch to deploy: main
   Base directory: (leave empty)
   Build command: (leave empty)
   Publish directory: (leave empty)
   ```
7. Click **"Deploy site"**
8. Wait 2-3 minutes

### Step 4: Customize Site Name (Optional)

1. In Netlify dashboard → **Site settings**
2. Click **"Change site name"**
3. Enter: `kpi-dashboard-5g`
4. Save
5. New URL: `https://kpi-dashboard-5g.netlify.app`

### Step 5: Note Your Dashboard URLs

```
5G Dashboard: https://kpi-dashboard-5g.netlify.app/dashboard.html
4G Dashboard: https://kpi-dashboard-5g.netlify.app/dashboard_4g.html
```

---

## Testing

### Test Checklist

#### ✅ Backend API Tests

```powershell
# 1. Health check
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/"

# 2. NC list
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/api/nc-list"

# 3. Availability data
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/api/availability?nc=All"

# 4. 4G data
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/api/4g-availability?nc=All"
```

#### ✅ Frontend Dashboard Tests

**5G Dashboard:**
1. Open: `https://kpi-dashboard-5g.netlify.app/dashboard.html`
2. Check loading spinner appears
3. Check NC dropdown loads
4. Select NC → verify charts load
5. Try different NCs → charts update
6. Check all 12 charts render

**4G Dashboard:**
1. Open: `https://kpi-dashboard-5g.netlify.app/dashboard_4g.html`
2. Check loading spinner appears
3. Check NC dropdown loads
4. Select NC → verify charts load
5. Try different NCs → charts update
6. Check all 10 charts render

#### ✅ Browser Console Tests

Press F12 → Console tab:
- ❌ No CORS errors
- ❌ No 404 errors
- ❌ No connection errors
- ✅ Success messages

#### ✅ Mobile Tests

1. Open on smartphone
2. Or use browser: F12 → Toggle device toolbar
3. Check responsive layout
4. Test on different screen sizes

---

## Troubleshooting

### ❌ Problem: "Database connection failed"

**Symptoms:**
- API returns error
- Backend logs show connection timeout

**Solutions:**

1. **Check database is online:**
   ```powershell
   psql -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres
   ```

2. **Verify environment variables in Render:**
   - Dashboard → kpi-dashboard-backend → Environment
   - Check DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

3. **Check firewall:**
   - Database server firewall must allow Render IPs
   - PostgreSQL port 5432 must be open

4. **If using ngrok:**
   - Ngrok must be running
   - URL may have changed (check ngrok console)
   - Update DB_HOST in Render environment variables
   - Redeploy backend

---

### ❌ Problem: CORS Error

**Symptoms:**
```
Access to fetch at '...' from origin '...' has been blocked by CORS policy
```

**Solutions:**

1. **Check Flask-CORS installed:**
   ```python
   # In dashboard_backend.py line 11-12
   from flask_cors import CORS
   CORS(app)
   ```

2. **Check requirements.txt:**
   ```txt
   Flask-CORS==4.0.0
   ```

3. **Redeploy backend** on Render

---

### ❌ Problem: Charts Not Loading

**Symptoms:**
- Loading spinner forever
- Empty charts
- No data shown

**Solutions:**

1. **Check browser console (F12):**
   - Look for error messages
   - Check network tab for failed requests

2. **Verify API_BASE_URL:**
   - In `dashboard.html` line 367
   - In `dashboard_4g.html` line 352
   - Must match YOUR backend URL

3. **Test API directly:**
   ```
   https://kpi-dashboard-backend.onrender.com/api/nc-list
   ```

4. **Clear browser cache:**
   - Ctrl+Shift+Delete
   - Or hard refresh: Ctrl+Shift+R

---

### ❌ Problem: Backend "Cold Start" Slow

**Symptoms:**
- First request takes 15-30 seconds
- Dashboard loads slowly

**Explanation:**
Render free tier sleeps after 15 minutes of inactivity.

**Solutions:**

**Option A:** Accept it (it's free!)
- First load slow, then normal

**Option B:** Keep-alive service
1. Signup at https://cron-job.org (free)
2. Create cron job:
   - URL: `https://kpi-dashboard-backend.onrender.com/`
   - Interval: Every 10 minutes

**Option C:** Upgrade to paid
- Render paid plan: $7/month (no sleep)

---

### ❌ Problem: Ngrok URL Changed

**Symptoms:**
- Dashboard stopped working
- Database connection failed
- Was working yesterday

**Explanation:**
Ngrok free tier URL changes every restart.

**Solutions:**

1. **Get new ngrok URL:**
   ```powershell
   ngrok tcp 5432
   ```

2. **Update backend environment variables:**
   - Render dashboard → kpi-dashboard-backend
   - Environment → DB_HOST
   - Update to new ngrok URL
   - Click "Save"

3. **Trigger redeploy:**
   - Manual Deploy → "Deploy latest commit"

**Permanent Solution:**
- Upgrade ngrok to paid ($8/month) for fixed domain
- OR use public IP address
- OR migrate database to cloud (Supabase/Render)

---

### ❌ Problem: 502 Bad Gateway

**Symptoms:**
Backend shows 502 error in Render logs.

**Solutions:**

1. **Check Render logs:**
   - Dashboard → kpi-dashboard-backend → Logs
   - Look for error messages

2. **Common issues:**
   - Port binding error → check Procfile
   - Import errors → check requirements.txt
   - Syntax errors → check code

3. **Verify Procfile:**
   ```
   web: gunicorn dashboard_backend:app --bind 0.0.0.0:$PORT
   ```

4. **Check runtime.txt:**
   ```
   python-3.11.0
   ```

---

## Monitoring & Maintenance

### Regular Checks

#### Daily
- ✅ Check dashboard loads
- ✅ Verify data updates

#### Weekly
- ✅ Check Render logs for errors
- ✅ Verify database connectivity
- ✅ Test all API endpoints

#### Monthly
- ✅ Review Render usage (free tier limits)
- ✅ Update dependencies if needed
- ✅ Backup database

### Render Free Tier Limits

| Resource | Limit |
|----------|-------|
| Build Minutes | 500 minutes/month |
| Bandwidth | 100 GB/month |
| Hours | 750 hours/month (1 service) |
| Sleep | After 15 min inactive |

**Note**: 750 hours = 31.25 days, enough for 1 service running 24/7!

### Updating the Dashboard

#### Update Code:
```powershell
# Make changes
git add .
git commit -m "Update: your description"
git push origin main

# Render auto-deploys on push!
# Netlify auto-deploys on push! (if using GitHub method)
```

#### Update Backend Only:
```powershell
# Edit dashboard_backend.py
git add dashboard_backend.py
git commit -m "Update backend"
git push

# Render auto-redeploys
```

#### Update Frontend Only:
```powershell
# Edit dashboard.html or dashboard_4g.html
git add dashboard*.html
git commit -m "Update frontend"
git push

# Netlify auto-redeploys (if using GitHub method)
# Or drag & drop new files (if using manual method)
```

### Logs & Debugging

#### View Backend Logs:
1. Render dashboard
2. Select: kpi-dashboard-backend
3. Click "Logs" tab
4. Real-time logs appear

#### View Netlify Logs:
1. Netlify dashboard
2. Select site
3. Click "Deploys"
4. View deploy logs

### Database Backup

```powershell
# Backup database
pg_dump -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres -F c -f backup_$(Get-Date -Format 'yyyyMMdd').dump

# Restore if needed
pg_restore -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres backup_20251031.dump
```

---

## 📊 Final Checklist

### Before Going Live:

- [ ] Database is accessible from internet
- [ ] Backend deployed to Render successfully
- [ ] Environment variables set correctly
- [ ] Backend health check returns 200 OK
- [ ] API endpoints return data
- [ ] Frontend deployed to Netlify
- [ ] API_BASE_URL updated in HTML files
- [ ] 5G dashboard loads and shows data
- [ ] 4G dashboard loads and shows data
- [ ] All charts rendering correctly
- [ ] Dropdown menus working
- [ ] Data updates when changing NC
- [ ] Mobile responsive working
- [ ] No console errors in browser
- [ ] GitHub repository up to date

---

## 🎯 Summary

### Your URLs:

```
📊 5G Dashboard:
https://kpi-dashboard-5g.netlify.app/dashboard.html

📊 4G Dashboard:
https://kpi-dashboard-5g.netlify.app/dashboard_4g.html

🔧 Backend API:
https://kpi-dashboard-backend.onrender.com

💾 Database:
1.tcp.ap.ngrok.io:21039 (or your server IP)

📁 GitHub Repo:
https://github.com/cashewwww14/kpi-dashboard
```

### Cost Breakdown:

| Service | Cost |
|---------|------|
| Database (Your Server) | $0 |
| Backend (Render) | $0 (Free tier) |
| Frontend (Netlify) | $0 (Free tier) |
| **Total** | **$0/month** 🎉 |

### Quick Commands:

```powershell
# Update and deploy
git add .
git commit -m "Update"
git push origin main

# Test backend locally
python dashboard_backend.py

# Test API
Invoke-WebRequest -Uri "https://kpi-dashboard-backend.onrender.com/api/nc-list"

# Database backup
pg_dump -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres -F c -f backup.dump
```

---

## 🎉 Congratulations!

Your KPI Dashboard is now:
- ✅ Fully deployed to cloud
- ✅ Accessible from anywhere
- ✅ Free to run (24/7)
- ✅ Auto-updates on git push
- ✅ HTTPS enabled
- ✅ Mobile responsive

---

## 📞 Support

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) section
2. Check Render logs for backend errors
3. Check browser console for frontend errors
4. Verify database connectivity
5. Test API endpoints directly

---

## 📚 Additional Resources

- Render Docs: https://render.com/docs
- Netlify Docs: https://docs.netlify.com
- Flask Docs: https://flask.palletsprojects.com
- Chart.js Docs: https://www.chartjs.org/docs

---

**Last Updated:** October 31, 2025
**Version:** 1.0
