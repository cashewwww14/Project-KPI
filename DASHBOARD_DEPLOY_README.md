# 🚀 5G KPI Dashboard - Deployment Guide

Dashboard ini dibuat untuk menggantikan Grafana yang tidak support variables di public deployment. Dashboard ini bisa di-deploy **GRATIS** ke berbagai platform.

## 📋 Fitur

✅ **Dropdown NC Selector** - Filter berdasarkan Network Cluster (termasuk opsi "All")
✅ **12 Chart Interaktif** - Semua KPI dari Grafana dashboard Anda
✅ **Real-time Data** - Langsung dari PostgreSQL
✅ **Responsive Design** - Berfungsi di desktop & mobile
✅ **Gratis Deploy** - Bisa di-deploy ke Render, Railway, atau Vercel

## 📊 Chart yang Tersedia

1. **Availability (%)** - avail_auto_5g × 100
2. **Accessibility** - da_5g
3. **Call Drop Rate** - g5_cdr
4. **SGNB Addition SR (%)** - sgnb_addition_sr × 100
5. **Traffic 5G (GB)** - traffic_5g
6. **EUT vs DL User Thp** - g5_eut_bhv vs g5_userdl_thp (stacked)
7. **User 5G** - sum_en_dc_user_5g_wd (bar chart)
8. **DL PRB Utilization vs Count > 85%** - g5_dlprb_util vs dl_prb_util_5g_count_gt_085
9. **Inter-eSgNB PSCell Change (%)** - inter_esgnb × 100
10. **Intra-eSgNB PSCell Change (%)** - intra_esgnb × 100
11. **Intra-SgNB Intrafreq PSCell Change (%)** - intra_sgnb_intrafreq × 100
12. **Inter-SgNB Intrafreq PSCell Change (%)** - inter_sgnb_intrafreq × 100

## 🛠️ Local Development

### 1. Install Dependencies

```bash
pip install -r requirements_dashboard.txt
```

### 2. Konfigurasi Database

Edit file `.env.dashboard`:

```env
DB_HOST=1.tcp.ap.ngrok.io
DB_PORT=21039
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=option88
PORT=5000
```

### 3. Jalankan Backend

```bash
python dashboard_backend.py
```

Backend akan berjalan di `http://localhost:5000`

### 4. Buka Dashboard

Buka `dashboard.html` di browser, atau jalankan:

```bash
# Windows
start dashboard.html

# Linux/Mac
open dashboard.html
```

## 🌐 Deploy ke Render.com (GRATIS)

Render.com menyediakan **free tier** untuk web service.

### Step 1: Push ke GitHub

```bash
git init
git add .
git commit -m "Initial commit - 5G KPI Dashboard"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO-NAME.git
git push -u origin main
```

### Step 2: Deploy di Render

1. Buka [render.com](https://render.com) dan signup/login
2. Click **"New +"** → **"Web Service"**
3. Connect repository GitHub Anda
4. Konfigurasi:
   - **Name**: `5g-kpi-dashboard`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements_dashboard.txt`
   - **Start Command**: `gunicorn dashboard_backend:app`
   - **Instance Type**: `Free`

5. **Environment Variables** (klik "Advanced"):
   ```
   DB_HOST=1.tcp.ap.ngrok.io
   DB_PORT=21039
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=option88
   ```

6. Click **"Create Web Service"**

7. Tunggu ~5-10 menit untuk deployment selesai

8. Anda akan dapat URL seperti: `https://5g-kpi-dashboard.onrender.com`

### Step 3: Update Frontend

Edit `dashboard.html`, ganti baris ini:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

Menjadi:

```javascript
const API_BASE_URL = 'https://5g-kpi-dashboard.onrender.com/api';
```

### Step 4: Deploy Frontend

#### Opsi A: Netlify (Recommended)

1. Buka [netlify.com](https://netlify.com)
2. Drag & drop file `dashboard.html` ke Netlify Drop
3. Selesai! Anda dapat URL seperti `https://random-name.netlify.app`

#### Opsi B: GitHub Pages

1. Push `dashboard.html` ke GitHub
2. Rename menjadi `index.html`
3. Di repository settings → Pages → Enable GitHub Pages
4. URL: `https://USERNAME.github.io/REPO-NAME/`

## 🚀 Deploy ke Railway.app (GRATIS)

Railway menyediakan $5 credit gratis per bulan.

### Step 1: Deploy Backend

1. Buka [railway.app](https://railway.app)
2. Click **"Start a New Project"**
3. Pilih **"Deploy from GitHub repo"**
4. Connect repository Anda
5. Railway akan auto-detect Python dan deploy
6. Tambahkan **Environment Variables**:
   ```
   DB_HOST=1.tcp.ap.ngrok.io
   DB_PORT=21039
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=option88
   ```
7. Generate domain: Settings → Generate Domain
8. Anda dapat URL seperti: `https://xxx.up.railway.app`

### Step 2: Update & Deploy Frontend

Sama seperti Render (Step 3 & 4 di atas).

## 🌍 Deploy ke Vercel (GRATIS)

Vercel gratis untuk hobby projects.

### Backend di Vercel

Buat file `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "dashboard_backend.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "dashboard_backend.py"
    }
  ]
}
```

Deploy:

```bash
npm i -g vercel
vercel login
vercel
```

Tambahkan environment variables di Vercel dashboard.

### Frontend di Vercel

```bash
vercel --prod dashboard.html
```

## 🔧 Troubleshooting

### CORS Error

Jika ada CORS error, pastikan `Flask-CORS` terinstall dan diaktifkan di `dashboard_backend.py`.

### Database Connection Failed

1. Pastikan ngrok tunnel masih aktif
2. Pastikan credentials database benar
3. Test koneksi: `psql -h 1.tcp.ap.ngrok.io -p 21039 -U postgres -d postgres`

### Chart Tidak Muncul

1. Buka browser console (F12) untuk lihat error
2. Pastikan API_BASE_URL di `dashboard.html` sudah benar
3. Test API endpoint: `curl http://localhost:5000/api/nc-list`

## 📱 Akses Mobile

Dashboard sudah responsive! Buka URL deployment dari smartphone Anda.

## 🔒 Security Notes

⚠️ **IMPORTANT**: Untuk production:

1. **Jangan commit credentials** - Use environment variables
2. **Enable HTTPS** - Render/Railway/Vercel sudah auto HTTPS
3. **Rate Limiting** - Tambahkan Flask-Limiter untuk prevent abuse
4. **Authentication** - Tambahkan basic auth jika perlu

## 💡 Tips

- **Free tier limitations**: 
  - Render: Service sleep setelah 15 menit inactive (restart otomatis saat diakses)
  - Railway: $5/month credit (cukup untuk hobby project)
  - Vercel: 100GB bandwidth/month
  
- **Ngrok alternative**: Gunakan database cloud (PostgreSQL di Render/Railway) agar lebih stabil

- **Monitoring**: Setup uptime monitoring gratis di uptimerobot.com

## 📞 Support

Jika ada masalah, check:
1. Backend logs di platform dashboard (Render/Railway/Vercel)
2. Browser console untuk frontend errors
3. Database connection dengan psql/pgAdmin

## 🎉 Selesai!

Dashboard Anda sekarang bisa diakses public dengan dropdown NC selector yang berfungsi!

**Backend URL**: `https://your-app.onrender.com`
**Frontend URL**: `https://your-site.netlify.app`

Selamat! 🚀
