# InnovaSoft - Enterprise AI & Software Solutions

![InnovaSoft Logo](https://innovasoft-landing.vercel.app/logo_white.png)

**InnovaSoft** is a high-performance, modern landing page designed for a forward-thinking software development agency specializing in Enterprise AI and tailor-made software solutions. Built with a focus on aesthetics, performance, and user experience, it features a sleek glassmorphism design and a robust, secure backend for client communications.

## 🚀 Tech Stack

### Frontend
- **Framework:** [Vue.js 3](https://vuejs.org/) (Composition API)
- **Build Tool:** [Vite](https://vitejs.dev/)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/)
- **Icons:** [Lucide Vue](https://lucide.dev/)
- **Animations:** CSS3 & Vue Transitions

### Backend
- **Runtime:** [Python 3.11](https://www.python.org/)
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Email Service:** Google Gmail API (OAuth 2.0)
- **Validation:** Pydantic

### Deployment
- **Platform:** [Vercel](https://vercel.com/) (Serverless Functions for Python Backend)

## ✨ Features

- **Modern UI/UX:** "Sharp Glass" aesthetic with premium glassmorphism effects and smooth animations.
- **Fully Responsive:** Optimized for all devices, from mobile phones to large desktop screens.
- **Interactive Contact Form:**
  - Real-time validation.
  - **Admin Notifications:** Instant email alerts for new leads.
  - **Auto-Replies:** Professional, branded HTML email confirmation sent to the user immediately.
- **Secure Architecture:**
  - OAuth 2.0 authentication for email sending (no less secure apps).
  - Environment variable protection for all sensitive credentials.
  - CORS configured for security.

## 🛠️ Installation & Setup

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- Google Cloud Console Project (for Gmail API credentials)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/innovasoft-landing.git
cd innovasoft-landing
```

### 2. Frontend Setup
```bash
cd frontend
npm install
```

### 3. Backend Setup
```bash
cd ../backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the `backend/` directory with the following variables:

```env
# Email Configuration
SENDER_EMAIL=your-email@gmail.com
ADMIN_EMAIL=admin-email@gmail.com

# Google OAuth Credentials (JSON content minified in one line)
GOOGLE_CREDENTIALS_JSON={...}
TOKEN_JSON={...}

# Security & Branding
ALLOWED_ORIGINS=http://localhost:5173,https://your-vercel-app.vercel.app
LOGO_URL=https://your-vercel-app.vercel.app/logo_white.png
```

> **Note:** `GOOGLE_CREDENTIALS_JSON` and `TOKEN_JSON` are the contents of your Google Cloud `credentials.json` and the generated `token.json` file, respectively.

## 🏃‍♂️ Running Locally

### Start Backend
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```
*Backend runs on: `http://localhost:8000`*

### Start Frontend
```bash
cd frontend
npm run dev
```
*Frontend runs on: `http://localhost:5173`*

## ☁️ Deployment (Vercel)

This project is configured for seamless deployment on Vercel.

1.  **Push to GitHub/GitLab.**
2.  **Import Project in Vercel:**
    - Select the repository.
    - Framework Preset: **Vite**.
    - Root Directory: `./` (Leave as default).
3.  **Environment Variables:**
    - Copy all variables from your local `.env` to the Vercel Project Settings.
4.  **Deploy:** Vercel will automatically build the Vue frontend and deploy the Python backend as Serverless Functions.

## 📂 Project Structure

```
innovasoft-landing/
├── frontend/           # Vue.js Application
│   ├── src/
│   ├── public/
│   └── vite.config.js
├── backend/            # FastAPI Application
│   ├── routers/        # API Route Handlers
│   ├── services/       # External Services (Gmail)
│   ├── utils/          # Helper Functions & Templates
│   ├── models.py       # Pydantic Models
│   └── main.py         # App Entry Point
├── vercel.json         # Vercel Deployment Config
└── README.md           # Project Documentation
```

---

© 2024 InnovaSoft. All rights reserved.
