Absolutely — here’s your `README.md` reformatted in **Canvas-style Markdown**, meaning it's designed to be clean, sectioned, and visually appealing if pasted into **Notion, GitHub Canvas, Obsidian**, or other markdown-friendly editors.

---

### 🎨 Canvas-Friendly `README.md`

```md
# 📰 Tech News API

> A lightweight Flask-based API that delivers live technology news using [NewsAPI.org](https://newsapi.org/).  
> Powers the news feed on DJ Martin's personal portfolio site.

---

## 🔗 Live Links

- **API Endpoint**: [https://news-api-flask-xxxx.onrender.com/api/tech-news](https://news-api-flask-xxxx.onrender.com/api/tech-news)
- **Portfolio Site**: [https://geo222222.github.io/Me/](https://geo222222.github.io/Me/)

---

## ✅ Features

- 📡 Fetches real-time tech news (top 5 headlines)
- 🌐 CORS-enabled for frontend integration
- ⚙️ Easy-to-deploy Flask + Gunicorn backend
- 🚀 Render-ready with dynamic port and environment handling

---

## 📡 API Endpoints

### `GET /`
Returns a basic JSON welcome message.

### `GET /api/tech-news`
Returns JSON array of top 5 tech news articles.

**Example Response:**
```json
[
  {
    "title": "AI outperforms Wall Street traders",
    "url": "https://example.com/article"
  },
  ...
]
```

---

## 🛠️ Local Setup

### 1. Clone Repo

```bash
git clone https://github.com/Geo222222/news-api-flask.git
cd news-api-flask
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set API Key (Optional `.env` file)

```env
NEWS_API_KEY=your_api_key_here
```

### 5. Run Locally

```bash
python app.py
```

App will be live at: `http://localhost:5000/api/tech-news`

---

## 🌍 Deployment on Render

1. Push the repo to GitHub
2. Go to [Render.com](https://render.com)
3. Create a **New Web Service**
4. Set these options:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add Environment Variable:
   - `NEWS_API_KEY = your_news_api_key`
6. Click **Deploy** 🚀

---

## 🧰 Tech Stack

- [Python 3.x](https://python.org)
- [Flask](https://flask.palletsprojects.com/)
- [NewsAPI.org](https://newsapi.org/)
- [Gunicorn](https://gunicorn.org/)
- [Render.com](https://render.com/)

---

## 📄 License

MIT License © 2025 DJ Martin

---

## 👋 Contact

- 📬 Email: [djuvanemartin@gmail.com](mailto:djuvanemartin@gmail.com)
- 🌐 Portfolio: [geo222222.github.io/Me](https://geo222222.github.io/Me)
```