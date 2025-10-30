# 📋 Deployment Checklist

Track your deployment progress with this checklist.

---

## PHASE 1: PREPARATION (Today - Server Mati OK!) ✅

### 1.1 File Check
- [ ] `dashboard_backend.py` exists
- [ ] `dashboard.html` exists
- [ ] `dashboard_4g.html` exists
- [ ] `requirements_dashboard.txt` exists
- [ ] `runtime.txt` exists
- [ ] `Procfile` exists
- [ ] `.gitignore` exists
- [ ] `README.md` exists
- [ ] `QUICKSTART.md` exists
- [ ] `DEPLOYMENT_GUIDE.md` exists

### 1.2 Database Credentials
- [ ] Database host noted: `___________________`
- [ ] Database port noted: `___________________`
- [ ] Database name noted: `___________________`
- [ ] Database user noted: `___________________`
- [ ] Database password noted: `___________________`

### 1.3 Git Setup
- [ ] Git initialized: `git init`
- [ ] Main branch set: `git branch -M main`
- [ ] Files staged: `git add .`
- [ ] Files committed: `git commit -m "Initial commit"`

### 1.4 GitHub Setup
- [ ] GitHub account ready
- [ ] New repository created: https://github.com/cashewwww14/kpi-dashboard
- [ ] Remote added: `git remote add origin ...`
- [ ] Code pushed: `git push -u origin main`

**✅ PREPARATION COMPLETE!** Repository ready for deployment.

---

## PHASE 2: BACKEND DEPLOYMENT (When Server Online) 🚀

### 2.1 Render Account
- [ ] Render account created: https://render.com
- [ ] Email verified
- [ ] Logged in to dashboard

### 2.2 Database Verification
- [ ] Database server is running
- [ ] Can connect to database: `psql -h ... -p ... -U postgres`
- [ ] Tables exist: `cluster_5g`, `cluster_4g`
- [ ] Data present: `SELECT COUNT(*) FROM cluster_5g;`

### 2.3 Deploy Backend
- [ ] Clicked "New +" → "Web Service"
- [ ] Connected GitHub account
- [ ] Selected repository: `kpi-dashboard`
- [ ] Configured build settings:
  - [ ] Name: `kpi-dashboard-backend`
  - [ ] Region: `Singapore` (or closest)
  - [ ] Runtime: `Python 3`
  - [ ] Build: `pip install -r requirements_dashboard.txt`
  - [ ] Start: `gunicorn dashboard_backend:app --bind 0.0.0.0:$PORT`
  - [ ] Instance Type: `Free`

### 2.4 Environment Variables
Added all variables:
- [ ] `DB_HOST` = `___________________`
- [ ] `DB_PORT` = `___________________`
- [ ] `DB_NAME` = `___________________`
- [ ] `DB_USER` = `___________________`
- [ ] `DB_PASSWORD` = `___________________`
- [ ] `PORT` = `10000`

### 2.5 Deployment
- [ ] Clicked "Create Web Service"
- [ ] Waited for deployment (5-10 minutes)
- [ ] Status shows "Live" (green)
- [ ] Backend URL noted: `https://_____________________.onrender.com`

### 2.6 Backend Testing
- [ ] Health check works: `https://your-backend.onrender.com/`
- [ ] NC list works: `https://your-backend.onrender.com/api/nc-list`
- [ ] Availability works: `https://your-backend.onrender.com/api/availability?nc=All`
- [ ] 4G data works: `https://your-backend.onrender.com/api/4g-availability?nc=All`
- [ ] No errors in Render logs

**✅ BACKEND DEPLOYED!** API is live.

---

## PHASE 3: FRONTEND DEPLOYMENT 🎨

### 3.1 Update Frontend Files

#### Update `dashboard.html`
- [ ] Opened `dashboard.html` in editor
- [ ] Found line 367: `const API_BASE_URL = ...`
- [ ] Changed to: `https://your-backend.onrender.com/api`
- [ ] Saved file

#### Update `dashboard_4g.html`
- [ ] Opened `dashboard_4g.html` in editor
- [ ] Found line 352: `const API_BASE_URL = ...`
- [ ] Changed to: `https://your-backend.onrender.com/api`
- [ ] Saved file

### 3.2 Commit Changes
- [ ] Staged changes: `git add dashboard.html dashboard_4g.html`
- [ ] Committed: `git commit -m "Update API URL for production"`
- [ ] Pushed: `git push origin main`

### 3.3 Netlify Account
- [ ] Netlify account created: https://netlify.com
- [ ] Email verified
- [ ] Logged in to dashboard

### 3.4 Deploy Frontend

**Option A: Drag & Drop**
- [ ] Clicked "Add new site" → "Deploy manually"
- [ ] Dragged `dashboard.html` and `dashboard_4g.html`
- [ ] Upload completed
- [ ] Site URL noted: `https://_____________________.netlify.app`

**Option B: GitHub (Recommended)**
- [ ] Clicked "Add new site" → "Import from GitHub"
- [ ] Authorized Netlify on GitHub
- [ ] Selected repository: `kpi-dashboard`
- [ ] Left all build settings empty
- [ ] Clicked "Deploy site"
- [ ] Waited for deployment (2-3 minutes)
- [ ] Status shows "Published" (green)
- [ ] Site URL noted: `https://_____________________.netlify.app`

### 3.5 Customize Domain (Optional)
- [ ] Went to Site settings
- [ ] Changed site name to: `kpi-dashboard-5g`
- [ ] New URL: `https://kpi-dashboard-5g.netlify.app`

**✅ FRONTEND DEPLOYED!** Dashboard is live.

---

## PHASE 4: TESTING & VERIFICATION 🧪

### 4.1 Backend Tests
- [ ] Health endpoint: `https://your-backend.onrender.com/`
- [ ] Returns: `{"message":"5G KPI Dashboard API","status":"running"}`
- [ ] NC list endpoint works
- [ ] All 5G endpoints return data
- [ ] All 4G endpoints return data
- [ ] No errors in browser console

### 4.2 5G Dashboard Tests
URL: `https://your-site.netlify.app/dashboard.html`
- [ ] Page loads without errors
- [ ] Loading spinner appears initially
- [ ] NC dropdown populates with values
- [ ] Can select "All" and see data
- [ ] All 12 charts render correctly:
  - [ ] Availability
  - [ ] Accessibility
  - [ ] Latency DL
  - [ ] Latency UL
  - [ ] Throughput DL
  - [ ] Throughput UL
  - [ ] EUtran vs DL Throughput
  - [ ] User 5G
  - [ ] DL PRB Utilization
  - [ ] (and 3 more...)
- [ ] Can switch between different NCs
- [ ] Charts update with new data
- [ ] No console errors (F12)

### 4.3 4G Dashboard Tests
URL: `https://your-site.netlify.app/dashboard_4g.html`
- [ ] Page loads without errors
- [ ] Loading spinner appears initially
- [ ] NC dropdown populates with values
- [ ] Can select "All" and see data
- [ ] All 10 charts render correctly:
  - [ ] Availability
  - [ ] Accessibility
  - [ ] EUtran Performance
  - [ ] DL PRB Utilization
  - [ ] UL PRB Utilization
  - [ ] CQI Distribution
  - [ ] User Active
  - [ ] Traffic Comparison
  - [ ] Traffic Percentage
  - [ ] (and 1 more...)
- [ ] Can switch between different NCs
- [ ] Charts update with new data
- [ ] No console errors (F12)

### 4.4 Mobile Tests
- [ ] Opened dashboard on smartphone
- [ ] OR used browser DevTools (F12) → Toggle device toolbar
- [ ] Layout is responsive
- [ ] Charts resize properly
- [ ] Dropdowns work on mobile
- [ ] No horizontal scrolling issues

### 4.5 Performance Tests
- [ ] Initial load time < 3 seconds (after first wake)
- [ ] Chart render time < 1 second
- [ ] NC switch time < 2 seconds
- [ ] Backend response time < 500ms

**✅ ALL TESTS PASSED!** Dashboard is production-ready.

---

## PHASE 5: DOCUMENTATION 📚

### 5.1 Save URLs
Backend API:
```
https://_____________________.onrender.com
```

5G Dashboard:
```
https://_____________________.netlify.app/dashboard.html
```

4G Dashboard:
```
https://_____________________.netlify.app/dashboard_4g.html
```

GitHub Repository:
```
https://github.com/cashewwww14/kpi-dashboard
```

### 5.2 Database Info
Database Host: `_____________________`
Database Port: `_____________________`
Database Name: `_____________________`

### 5.3 Important Notes
- [ ] Documented any issues encountered
- [ ] Noted first response time (cold start)
- [ ] Saved credentials securely
- [ ] Shared URLs with team (if needed)

**✅ DOCUMENTATION COMPLETE!**

---

## PHASE 6: POST-DEPLOYMENT (Optional) 🎯

### 6.1 Keep Backend Awake (Optional)
- [ ] Signed up at cron-job.org
- [ ] Created new cron job:
  - URL: `https://your-backend.onrender.com/`
  - Interval: Every 10 minutes
  - Enabled: Yes
- [ ] Verified cron job is working

### 6.2 Custom Domain (Optional)
- [ ] Purchased domain name
- [ ] Configured DNS in Netlify
- [ ] Updated backend CORS if needed
- [ ] SSL certificate auto-configured

### 6.3 Monitoring Setup (Optional)
- [ ] Enabled Render email notifications
- [ ] Enabled Netlify deploy notifications
- [ ] Set up uptime monitoring (UptimeRobot)

### 6.4 Analytics (Optional)
- [ ] Added Google Analytics to HTML
- [ ] Set up custom events for chart views
- [ ] Track NC selection patterns

**✅ POST-DEPLOYMENT COMPLETE!**

---

## 🎉 FINAL STATUS

### Summary
- ✅ Database: Connected and accessible
- ✅ Backend: Deployed to Render (Free)
- ✅ Frontend: Deployed to Netlify (Free)
- ✅ 5G Dashboard: Fully functional
- ✅ 4G Dashboard: Fully functional
- ✅ All tests: Passed
- ✅ Documentation: Complete

### Cost
- Database: $0 (your server)
- Backend: $0 (Render free tier)
- Frontend: $0 (Netlify free tier)
- **Total: $0/month** 🎉

### Next Steps
- [ ] Share dashboard URLs with stakeholders
- [ ] Monitor performance and errors
- [ ] Plan regular database backups
- [ ] Schedule periodic testing
- [ ] Consider upgrading if needed

---

**🚀 DEPLOYMENT SUCCESSFUL!**

**Date Completed:** `___________________`

**Total Time:** `___________________`

**Deployed By:** `___________________`

---

## 📞 Quick Reference

### Useful Commands

**Git:**
```powershell
git status                          # Check status
git add .                           # Stage changes
git commit -m "message"             # Commit
git push origin main                # Push to GitHub
```

**Database:**
```powershell
psql -h HOST -p PORT -U USER -d DB  # Connect to database
pg_dump ... -f backup.dump          # Backup database
```

**Testing:**
```powershell
# Test backend
Invoke-WebRequest -Uri "https://your-backend.onrender.com/api/nc-list"

# Run preparation script
.\prepare-deploy.ps1
```

### Support Resources
- 📖 [README.md](README.md)
- 📖 [QUICKSTART.md](QUICKSTART.md)
- 📖 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- 🌐 [Render Docs](https://render.com/docs)
- 🌐 [Netlify Docs](https://docs.netlify.com)

---

**Good luck with your deployment! 🎉**
