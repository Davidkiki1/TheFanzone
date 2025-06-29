# ⚽ Fanzone

**Fanzone** is a full-stack web application built for football fans to view player stats, comment, and interact with clubs and players. It includes user authentication, session management, and real-time fan engagement features.

---

## 🚀 Technologies Used

### 🔧 Backend (Flask)
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask-CORS
- Flask-Login (session-based auth)
- PostgreSQL (Render-hosted)
- Blueprints for modular routing

### 🎨 Frontend (React)
- React Router v5
- Context API for authentication
- Fetch API for data communication
- React state & events
- CSS (App-specific styles)

---

## 📁 Project Structure

fanzone/
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ ├── player_routes.py
│ │ ├── fanpost_routes.py
│ │ └── comment_routes.py
│ ├── migrations/
│ ├── seed.py
│ └── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── context/
│ │ ├── App.js
│ │ └── index.js
│ └── package.json
└── README.md

yaml
Copy
Edit

---

## 🌐 Live Demo

🔗 Backend API: [https://fanzone-backend.onrender.com](https://fanzone-backend.onrender.com)  
🔗 Frontend: [https://fanzone.onrender.com](https://fanzone.onrender.com)

---

## 🧠 Features

### 🔐 Authentication
- Signup, login, and logout with sessions
- Session persistence using `/check_session`
- Protected features like commenting and fanposting

### 🧍‍♂️ Player Section
- Browse all players
- View stats, comments, and former clubs
- Logged-in users can comment

### 🏟️ Club Section
- View clubs and their trophies
- Players linked to current and former clubs

### 💬 Fanposts
- Fans can post, edit, and delete posts
- Logged-in users only

### 🧼 Extras
- Team logos and player images
- Styled UI
- Blueprint routing and clean MVC structure

---

## 📦 Backend Setup (Local)

```bash
# Clone the repo
git clone https://github.com/Davidkiki1/fanzone.git
cd fanzone/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
flask db upgrade

# Seed database (optional)
python seed.py

# Run app
flask run
🖥️ Frontend Setup (Local)
bash
Copy
Edit
cd fanzone/frontend

# Install dependencies
npm install

# Start development server
npm start
🌍 Deployment (Render)
🔸 Backend (Flask)
Create a Web Service on Render.

Connect your GitHub repo.

Set:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Add environment variables:

FLASK_ENV=production

DATABASE_URL (from Render PostgreSQL service)

SECRET_KEY (your secret key)

🔸 Frontend (React)
Create a Static Site on Render.

Set:

Build Command: npm run build

Publish Directory: build

(Optional) Add environment variables for API base URL.

🛠️ Environment Variables
Key	Description
FLASK_ENV	production or development
DATABASE_URL	PostgreSQL DB URI (Render-provided)
SECRET_KEY	Flask session key

🙋‍♂️ Author
Made with ❤️ by David Kiki

