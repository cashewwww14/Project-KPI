# 📊 5G & 4G KPI Dashboard

Real-time monitoring dashboard untuk Network Performance KPI (Key Performance Indicators) 5G dan 4G.

![Dashboard Preview](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### 5G Dashboard
- 📈 Availability & Accessibility Monitoring
- 📊 12 Real-time Performance Charts
- 🎯 Latency Analysis (DL/UL)
- 📡 Throughput Monitoring
- 👥 User Distribution Analysis
- 🔄 Resource Block Utilization

### 4G Dashboard
- 📈 Availability & Accessibility Monitoring
- 📊 10 Real-time Performance Charts
- 🎯 EUtran Performance
- 📡 PRB Utilization
- 📶 CQI Distribution
- 👥 User & Traffic Analysis

## 🏗️ Architecture

```
Database Server (PostgreSQL)
        ↓
Backend API (Flask)
        ↓
Frontend Dashboard (HTML/JS/Chart.js)
```

## 🚀 Quick Start

### Option 1: Deploy to Cloud (Recommended)

**📖 Read:** [`QUICKSTART.md`](QUICKSTART.md) - Deployment dalam 15 menit

**Step-by-step:**
1. Run preparation script:
   ```powershell
   .\prepare-deploy.ps1
   ```

2. Follow instructions in [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md)

**Result:**
- ✅ Backend deployed to Render (Free)
- ✅ Frontend deployed to Netlify (Free)
- ✅ Accessible from anywhere
- ✅ HTTPS enabled
- ✅ Auto-deploy on git push

### Option 2: Run Locally

1. **Install Dependencies:**
   ```powershell
   pip install -r requirements_dashboard.txt
   ```

2. **Configure Database:**
   ```powershell
   # Copy example env file
   copy .env.example .env.dashboard
   
   # Edit .env.dashboard with your database credentials
   notepad .env.dashboard
   ```

3. **Run Backend:**
   ```powershell
   python dashboard_backend.py
   ```

4. **Open Dashboard:**
   ```
   http://localhost:5000/dashboard.html
   http://localhost:5000/dashboard_4g.html
   ```

## 📁 Project Structure

```
Project-KPI/
├── 📄 dashboard_backend.py         # Flask API backend
├── 📄 dashboard.html               # 5G KPI Dashboard
├── 📄 dashboard_4g.html            # 4G KPI Dashboard
├── 📄 requirements_dashboard.txt   # Python dependencies
├── 📄 runtime.txt                  # Python version
├── 📄 Procfile                     # Deploy configuration
├── 📄 .env.example                 # Environment template
├── 📄 .gitignore                   # Git ignore rules
├── 📄 README.md                    # This file
├── 📄 QUICKSTART.md                # Quick deployment guide
├── 📄 DEPLOYMENT_GUIDE.md          # Complete deployment docs
└── 📄 prepare-deploy.ps1           # Deployment prep script
```

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **psycopg 3.1.18** - PostgreSQL adapter
- **Flask-CORS 4.0.0** - CORS handling
- **Gunicorn 21.2.0** - WSGI server

### Frontend
- **HTML5 / CSS3** - Structure & styling
- **JavaScript (ES6+)** - Logic & interaction
- **Chart.js** - Data visualization
- **Responsive Design** - Mobile-friendly

### Database
- **PostgreSQL** - Data storage
- Tables: `cluster_5g`, `cluster_4g`

### Deployment
- **Render.com** - Backend hosting (Free)
- **Netlify** - Frontend hosting (Free)
- **GitHub** - Version control & CI/CD

## 📊 API Endpoints

### 5G Endpoints
```
GET /api/nc-list                    # Get NC list
GET /api/availability?nc=All        # Availability data
GET /api/accessibility?nc=All       # Accessibility data
GET /api/latency-dl?nc=All          # DL Latency
GET /api/latency-ul?nc=All          # UL Latency
GET /api/throughput-dl?nc=All       # DL Throughput
GET /api/throughput-ul?nc=All       # UL Throughput
GET /api/eut-vs-dl?nc=All           # EUtran vs DL
GET /api/user-5g?nc=All             # User distribution
GET /api/dl-prb-util?nc=All         # DL PRB utilization
```

### 4G Endpoints
```
GET /api/4g-availability?nc=All     # Availability data
GET /api/4g-accessibility?nc=All    # Accessibility data
GET /api/4g-eut?nc=All              # EUtran performance
GET /api/4g-dl-prb-util?nc=All      # DL PRB utilization
GET /api/4g-ul-prb-util?nc=All      # UL PRB utilization
GET /api/4g-cqi?nc=All              # CQI distribution
GET /api/4g-user?nc=All             # User active
GET /api/4g-traffic-comparison?nc=All # Traffic comparison
GET /api/4g-traffic-percent?nc=All  # Traffic percentage
```

## 🔒 Security

### Environment Variables
Sensitive data (database credentials) are stored in environment variables, not in code.

**Production:**
```
DB_HOST=your-database-host
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-secure-password
```

### CORS
Cross-Origin Resource Sharing enabled for frontend access.

### HTTPS
Automatically enabled on Render & Netlify deployments.

## 📈 Performance

- **Backend Response Time**: < 200ms (typical)
- **Frontend Load Time**: < 2s (initial load)
- **Chart Render Time**: < 500ms per chart
- **API Rate Limit**: No limit (add if needed)

## 🐛 Troubleshooting

### Database Connection Failed
```powershell
# Test database connection
psql -h YOUR_HOST -p YOUR_PORT -U postgres -d postgres
```

### CORS Error
Check `Flask-CORS` is installed and `CORS(app)` is called in backend.

### Charts Not Loading
1. Check browser console (F12) for errors
2. Verify `API_BASE_URL` in HTML files
3. Test API endpoints directly

### Backend Sleep (Render Free Tier)
First request may take 15-30 seconds. Use cron-job.org to keep alive.

**Full troubleshooting:** See [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md#troubleshooting)

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Quick deployment guide (15 min)
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete deployment documentation
- **[.env.example](.env.example)** - Environment variables template

## 🔄 Updates & Maintenance

### Update Code
```powershell
git add .
git commit -m "Your update message"
git push origin main
```

Both Render and Netlify will auto-deploy!

### Database Backup
```powershell
pg_dump -h YOUR_HOST -p YOUR_PORT -U postgres -d postgres -F c -f backup.dump
```

### View Logs
- **Render**: Dashboard → Your Service → Logs
- **Netlify**: Dashboard → Your Site → Deploys

## 💰 Cost

| Component | Service | Cost |
|-----------|---------|------|
| Database | Your Server | $0 |
| Backend | Render.com | $0 (Free tier) |
| Frontend | Netlify | $0 (Free tier) |
| **Total** | | **$0/month** 🎉 |

**Free Tier Limits:**
- Render: 750 hours/month (enough for 24/7)
- Netlify: 100GB bandwidth/month

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Open Pull Request

## 📝 License

MIT License - Feel free to use for personal or commercial projects.

## 👤 Author

**cashewwww14**
- GitHub: [@cashewwww14](https://github.com/cashewwww14)

## 🌟 Acknowledgments

- Chart.js for beautiful visualizations
- Flask for simple and powerful backend
- Render & Netlify for free hosting

## 📞 Support

Having issues? Check:
1. [Troubleshooting Guide](DEPLOYMENT_GUIDE.md#troubleshooting)
2. [GitHub Issues](https://github.com/cashewwww14/kpi-dashboard/issues)
3. Backend logs on Render
4. Browser console (F12)

---

## 🎯 Quick Links

### Live Demo
- 🌐 **5G Dashboard**: `https://your-site.netlify.app/dashboard.html`
- 🌐 **4G Dashboard**: `https://your-site.netlify.app/dashboard_4g.html`
- 🔧 **Backend API**: `https://your-backend.onrender.com`

### Resources
- 📖 [Flask Documentation](https://flask.palletsprojects.com)
- 📖 [Chart.js Documentation](https://www.chartjs.org/docs)
- 📖 [Render Documentation](https://render.com/docs)
- 📖 [Netlify Documentation](https://docs.netlify.com)

---

**⭐ Star this repository if you find it helpful!**

**Last Updated:** October 31, 2025
