# 🚀 Quick Start - Deploy KPI Dashboard

## ⚡ Super Cepat (15 menit)

### Prerequisites
- ✅ GitHub account
- ✅ Render.com account (gratis)
- ✅ Netlify account (gratis)
- ✅ Database server dengan PostgreSQL

---

## 📝 Preparation Checklist (SEKARANG - Server Mati OK!)

### ✅ Step 1: Cek File-File Project

```powershell
cd C:\Users\lenov\Documents\project\Project-KPI
dir
```

Pastikan ada:
- [ ] `dashboard_backend.py` - Backend API
- [ ] `dashboard.html` - 5G Dashboard
- [ ] `dashboard_4g.html` - 4G Dashboard
- [ ] `requirements_dashboard.txt` - Dependencies
- [ ] `runtime.txt` - Python version
- [ ] `Procfile` - Deploy config
- [ ] `.gitignore` - Git ignore rules
- [ ] `.env.example` - Environment template
- [ ] `DEPLOYMENT_GUIDE.md` - Full guide

### ✅ Step 2: Catat Database Credentials

Walaupun server mati, catat dulu credentials-nya:

```
Database Host: 1.tcp.ap.ngrok.io (atau IP server kamu)
Database Port: 21039 (atau 5432)
Database Name: postgres
Database User: postgres
Database Password: option88
```

**📝 Simpan info ini!** Nanti dipake di Render.

### ✅ Step 3: Initialize Git

```powershell
# Initialize git
git init

# Set main branch
git branch -M main

# Add all files
git add .

# Commit
git commit -m "Initial commit: 5G & 4G KPI Dashboard"
```

### ✅ Step 4: Create GitHub Repository

1. Buka: https://github.com/new
2. Repository name: `kpi-dashboard`
3. Public
4. **JANGAN** centang "Initialize with README"
5. Create repository

### ✅ Step 5: Push ke GitHub

```powershell
# Add remote (ganti username!)
git remote add origin https://github.com/cashewwww14/kpi-dashboard.git

# Push
git push -u origin main
```

**🎉 PREPARATION DONE!** Repository sudah siap untuk deploy.

---

## 🚀 Deployment (Nanti - Saat Server Nyala)

### PART 1: Deploy Backend (10 menit)

1. **Login Render**: https://dashboard.render.com
2. **New +** → **Web Service**
3. **Connect GitHub** → pilih `kpi-dashboard`
4. **Configure**:
   ```
   Name: kpi-dashboard-backend
   Region: Singapore
   Runtime: Python 3
   Build: pip install -r requirements_dashboard.txt
   Start: gunicorn dashboard_backend:app --bind 0.0.0.0:$PORT
   ```
5. **Environment Variables** (PENTING!):
   ```
   DB_HOST=1.tcp.ap.ngrok.io
   DB_PORT=21039
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=option88
   ```
6. **Create Web Service**
7. **Tunggu 5-10 menit**
8. **Save URL**: `https://kpi-dashboard-backend.onrender.com`

### PART 2: Update Frontend (2 menit)

#### Update `dashboard.html` (line 367):
```javascript
// BEFORE
const API_BASE_URL = 'http://localhost:5000/api';

// AFTER (ganti dengan URL Render kamu!)
const API_BASE_URL = 'https://kpi-dashboard-backend.onrender.com/api';
```

#### Update `dashboard_4g.html` (line 352):
```javascript
// BEFORE
const API_BASE_URL = 'http://localhost:5000/api';

// AFTER (ganti dengan URL Render kamu!)
const API_BASE_URL = 'https://kpi-dashboard-backend.onrender.com/api';
```

#### Commit changes:
```powershell
git add dashboard.html dashboard_4g.html
git commit -m "Update API URL for production"
git push origin main
```

### PART 3: Deploy Frontend (3 menit)

#### Option A: Drag & Drop (Termudah)
1. Login: https://app.netlify.com
2. **Add new site** → **Deploy manually**
3. Drag 2 files: `dashboard.html` & `dashboard_4g.html`
4. Done! Get URL: `https://xxx.netlify.app`

#### Option B: GitHub (Auto-deploy)
1. Login: https://app.netlify.com
2. **Add new site** → **Import from GitHub**
3. Select: `kpi-dashboard`
4. Deploy settings: (kosongkan semua)
5. **Deploy**

### PART 4: Test! (1 menit)

```
✅ Backend: https://kpi-dashboard-backend.onrender.com
✅ 5G Dashboard: https://xxx.netlify.app/dashboard.html
✅ 4G Dashboard: https://xxx.netlify.app/dashboard_4g.html
```

---

## 🔧 Quick Troubleshooting

### Database Connection Failed?
- ✅ Database server nyala?
- ✅ Ngrok running? (kalau pakai ngrok)
- ✅ Environment variables benar?
- ✅ Firewall allow port 5432?

### Charts Not Loading?
- ✅ API_BASE_URL sudah diganti?
- ✅ Hard refresh: Ctrl+Shift+R
- ✅ Check console (F12) untuk errors

### Backend Sleep?
- ✅ Normal! Render free tier sleep after 15 min
- ✅ First load akan lambat (15-30 detik)
- ✅ Setup cron-job.org untuk keep-alive

---

## 📋 Important URLs

```
GitHub: https://github.com/cashewwww14/kpi-dashboard
Render: https://dashboard.render.com
Netlify: https://app.netlify.com
```

---

## 💡 Tips

1. **Ngrok URL berubah?**
   - Update `DB_HOST` di Render environment variables
   - Redeploy backend

2. **Auto-deploy on push:**
   - Render: Auto-deploy saat push ke GitHub
   - Netlify: Auto-deploy saat push ke GitHub (kalau pakai option B)

3. **Free tier limits:**
   - Render: 750 jam/bulan (cukup 1 service 24/7)
   - Netlify: 100GB bandwidth/bulan

4. **Keep backend awake:**
   - Cron-job.org ping setiap 10 menit
   - URL: `https://kpi-dashboard-backend.onrender.com/`

---

## 📚 Full Documentation

Baca guide lengkap: [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md)

---

## ✅ Checklist Summary

### Today (Server Mati - OK!)
- [x] Check all files exist
- [x] Note database credentials
- [x] Initialize git
- [x] Create GitHub repo
- [x] Push to GitHub
- [ ] **READY TO DEPLOY!** ✨

### Next (Server Nyala)
- [ ] Start database server
- [ ] Deploy backend to Render
- [ ] Update frontend API URLs
- [ ] Deploy frontend to Netlify
- [ ] Test everything
- [ ] **LIVE!** 🚀

---

**Total Time**: 
- Preparation (now): ~10 minutes ✅
- Deployment (later): ~15 minutes ⏳
- **Total**: ~25 minutes 🎉
