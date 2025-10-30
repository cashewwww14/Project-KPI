# 🚀 Panduan Deploy Frontend KPI Dashboard (GRATIS)

## ✅ Status Backend
Backend sudah di-deploy di: https://kpi-dashboard-backend-4j5e.onrender.com/

URL backend sudah di-update di kedua file dashboard (`dashboard.html` dan `dashboard_4g.html`).

---

## 📋 Pilihan Platform Hosting Gratis untuk Frontend

Ada beberapa pilihan platform gratis untuk hosting HTML/CSS/JavaScript:

### 🌟 **Opsi 1: GitHub Pages (Paling Mudah & Recommended)**
- ✅ Gratis selamanya
- ✅ Unlimited bandwidth
- ✅ Custom domain support
- ✅ HTTPS otomatis
- ✅ Cocok untuk static HTML

### 🌟 **Opsi 2: Netlify**
- ✅ Gratis untuk personal projects
- ✅ 100GB bandwidth/bulan
- ✅ Continuous deployment
- ✅ HTTPS otomatis
- ✅ Custom domain support

### 🌟 **Opsi 3: Vercel**
- ✅ Gratis untuk personal use
- ✅ 100GB bandwidth/bulan
- ✅ Global CDN
- ✅ HTTPS otomatis

### 🌟 **Opsi 4: Cloudflare Pages**
- ✅ Gratis unlimited
- ✅ Bandwidth unlimited
- ✅ Global CDN
- ✅ HTTPS otomatis

---

## 🎯 METODE 1: GITHUB PAGES (Paling Mudah)

### Step 1: Siapkan Repository di GitHub

1. **Buka GitHub** dan pastikan kamu sudah login
   - Website: https://github.com

2. **Buka repository kamu**: `cashewwww14/Project-KPI`
   - Atau buat repository baru jika belum ada

3. **Push file dashboard ke GitHub** (jika belum):
   ```powershell
   cd "c:\Users\lenov\Documents\project\Project-KPI"
   git add dashboard.html dashboard_4g.html
   git commit -m "Update backend URL for deployment"
   git push origin main
   ```

### Step 2: Aktifkan GitHub Pages

1. **Buka Settings Repository**
   - Masuk ke repository: https://github.com/cashewwww14/Project-KPI
   - Klik tab **"Settings"** (pojok kanan atas)

2. **Konfigurasi GitHub Pages**
   - Di sidebar kiri, cari dan klik **"Pages"**
   - Di bagian **"Source"**:
     - Branch: Pilih `main` (atau `master`)
     - Folder: Pilih `/ (root)`
   - Klik **"Save"**

3. **Tunggu Deployment** (1-2 menit)
   - GitHub akan otomatis deploy website kamu
   - URL akan muncul di bagian atas, contoh:
     ```
     https://cashewwww14.github.io/Project-KPI/
     ```

### Step 3: Akses Dashboard

Setelah deploy selesai, kamu bisa akses:
- **Dashboard 5G**: `https://cashewwww14.github.io/Project-KPI/dashboard.html`
- **Dashboard 4G**: `https://cashewwww14.github.io/Project-KPI/dashboard_4g.html`

### Step 4: Buat Landing Page (Opsional)

Buat file `index.html` di root agar user bisa pilih dashboard:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KPI Dashboard - Select Version</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            text-align: center;
            background: white;
            padding: 60px 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
        }
        h1 {
            color: #333;
            margin-bottom: 15px;
            font-size: 2.5em;
        }
        p {
            color: #666;
            margin-bottom: 40px;
            font-size: 1.1em;
        }
        .buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        .btn {
            padding: 20px 40px;
            font-size: 1.2em;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            text-decoration: none;
            color: white;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .btn-5g {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        }
        .btn-4g {
            background: linear-gradient(135deg, #0f9b0f 0%, #38b000 100%);
        }
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .info {
            margin-top: 40px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 KPI Dashboard</h1>
        <p>Pilih dashboard yang ingin Anda lihat</p>
        <div class="buttons">
            <a href="dashboard.html" class="btn btn-5g">
                5G Dashboard
            </a>
            <a href="dashboard_4g.html" class="btn btn-4g">
                4G Dashboard
            </a>
        </div>
        <div class="info">
            <strong>ℹ️ Informasi:</strong><br>
            Dashboard ini menampilkan Key Performance Indicators (KPI) untuk jaringan 5G dan 4G.
            Pilih dashboard sesuai dengan teknologi yang ingin Anda monitor.
        </div>
    </div>
</body>
</html>
```

Lalu push ke GitHub:
```powershell
git add index.html
git commit -m "Add landing page"
git push origin main
```

---

## 🎯 METODE 2: NETLIFY

### Step 1: Siapkan Akun Netlify

1. **Buka Netlify**: https://www.netlify.com/
2. **Sign Up** dengan akun GitHub (gratis)

### Step 2: Deploy via Drag & Drop

**Cara Paling Mudah (Manual Upload):**

1. Buat folder baru `frontend-deploy`
2. Copy file-file ini ke folder tersebut:
   - `dashboard.html`
   - `dashboard_4g.html`
   - `index.html` (jika sudah dibuat)

3. **Di Netlify Dashboard**:
   - Cari area **"Sites"**
   - Drag & drop folder `frontend-deploy` ke area yang bertulisan "Want to deploy a new site without connecting to Git? Drag and drop your site output folder here"
   - Tunggu beberapa detik

4. **Website Online!**
   - Netlify akan generate URL random seperti: `https://random-name-123.netlify.app`
   - Kamu bisa ganti nama di **Site settings → Change site name**

**Atau via GitHub (Otomatis):**

1. **Di Netlify Dashboard**:
   - Klik **"Add new site"** → **"Import an existing project"**
   - Pilih **"Deploy with GitHub"**
   - Authorize Netlify
   - Pilih repository: `cashewwww14/Project-KPI`

2. **Build Settings**:
   - Branch: `main`
   - Build command: (kosongkan)
   - Publish directory: `/` (root)
   - Klik **"Deploy site"**

3. **Selesai!**
   - URL: `https://your-site-name.netlify.app`

---

## 🎯 METODE 3: VERCEL

### Step 1: Siapkan Akun Vercel

1. **Buka Vercel**: https://vercel.com/
2. **Sign Up** dengan akun GitHub (gratis)

### Step 2: Deploy

1. **Di Vercel Dashboard**:
   - Klik **"Add New..."** → **"Project"**
   - Pilih **"Import Git Repository"**
   - Pilih repository: `cashewwww14/Project-KPI`

2. **Configure Project**:
   - Project Name: `kpi-dashboard` (atau nama lain)
   - Framework Preset: **Other**
   - Root Directory: `./` (root)
   - Build Command: (kosongkan)
   - Output Directory: (kosongkan)
   - Klik **"Deploy"**

3. **Selesai!**
   - URL: `https://kpi-dashboard.vercel.app` (atau nama yang kamu pilih)

---

## 🎯 METODE 4: CLOUDFLARE PAGES

### Step 1: Siapkan Akun Cloudflare

1. **Buka Cloudflare**: https://pages.cloudflare.com/
2. **Sign Up** (gratis)

### Step 2: Deploy

1. **Di Cloudflare Pages Dashboard**:
   - Klik **"Create a project"**
   - Pilih **"Connect to Git"**
   - Connect GitHub account
   - Pilih repository: `cashewwww14/Project-KPI`

2. **Configure Build**:
   - Project name: `kpi-dashboard`
   - Production branch: `main`
   - Build command: (kosongkan)
   - Build output directory: `/`
   - Klik **"Save and Deploy"**

3. **Selesai!**
   - URL: `https://kpi-dashboard.pages.dev`

---

## 🔧 Troubleshooting

### Problem: CORS Error saat akses backend

**Solusi**: Backend sudah di-configure dengan CORS. Jika masih error, pastikan URL backend benar:
```javascript
const API_BASE_URL = 'https://kpi-dashboard-backend-4j5e.onrender.com/api';
```

### Problem: Data tidak muncul di dashboard

**Cek**:
1. Apakah backend masih running? Cek: https://kpi-dashboard-backend-4j5e.onrender.com/
2. Buka browser DevTools (F12) → Console, lihat error messages
3. Pastikan backend punya data di database

### Problem: Backend "sleep" karena free tier Render

**Solusi**:
- Backend Render free tier sleep setelah 15 menit tidak digunakan
- Saat diakses pertama kali, tunggu 30-60 detik untuk "wake up"
- Atau upgrade ke paid plan ($7/bulan) untuk always-on

---

## 📝 Rekomendasi

**Untuk proyek ini, saya rekomendasikan GitHub Pages karena:**
- ✅ Paling mudah setup
- ✅ Gratis unlimited
- ✅ Cocok untuk static HTML
- ✅ Sudah punya repository di GitHub
- ✅ Tidak perlu konfigurasi build

**Jika butuh fitur lebih advance:**
- **Netlify/Vercel**: Untuk analytics, forms, serverless functions
- **Cloudflare Pages**: Untuk CDN global tercepat

---

## 🎉 Setelah Deploy

1. **Cek URL backend sudah benar** di kedua file HTML
2. **Test dashboard** dengan membuka URL yang sudah di-deploy
3. **Monitor** apakah data muncul dengan benar
4. **Share URL** ke tim atau client

---

## 📞 Bantuan Tambahan

Jika ada masalah, cek:
- Browser Console (F12 → Console tab)
- Network tab untuk lihat API requests
- Backend logs di Render dashboard

**Happy Deploying! 🚀**
