# Global Group of Education - Localhost Deployment

Website ka complete data prefetch ho chuka hai aur local server par live chal raha hai.

## 🚀 Quick Access

- **Localhost URL:** [http://localhost:8080](http://localhost:8080)
- **Local IP:** [http://127.0.0.1:8080](http://127.0.0.1:8080)

Server background mein chal raha hai. Aap browser khol kar directly `http://localhost:8080` visit kar sakte hain.

---

## 📂 Project Structure

```
├── public/
│   ├── assets/              # Downloaded CSS, JS, Fonts & Icons
│   ├── uploads/             # Downloaded University Logos & Media Images
│   └── pages/               # 120 HTML Pages (Links rewritten to /)
│       ├── home.html
│       ├── about-us.html
│       ├── contact-us.html
│       ├── study-in-uk.html
│       ├── study-in-usa.html
│       ├── all-universities.html
│       └── ...
├── fetched_data/
│   ├── site_data.json       # Complete Structured JSON database
│   ├── universities.json    # Partner universities details
│   ├── destinations.json    # Target study destinations
│   ├── courses.json         # Programs and courses catalog
│   └── site_summary.md      # Prefetch analytical report
├── server.py                # Python local server with dynamic routing & caching
└── start_server.bat         # 1-Click launcher for Windows
```

---

## 💡 Features
1. **Full Offline-First Capability**: Sabhi 120 pages, styling (Bootstrap, custom.css, FontAwesome, fonts) aur images local folder se serve hoti hain.
2. **Local Routing**: Internal navigation links local files par switch ho gaye hain (bina live site par redirect huye).
3. **Smart Cache Fallback**: Agar koi un-cached asset request hoti hai to server use fetch karke local cache mein save karta hai.
