# 🚀 Deployment Guide: AI Hari Raya Greeting Generator

Follow these steps to deploy your application to **Streamlit Community Cloud** for free and share it with your friends securely.

---

## 📋 Prerequisites
1. A **GitHub** account.
2. A **Streamlit Community Cloud** account (sign up at [share.streamlit.io](https://share.streamlit.io/) using your GitHub).
3. Your **Google Gemini API Key**.

---

## 🛠️ Step 1: Prepare Your Repository
Before pushing to GitHub, you must ensure your private information (API Key) is **not** uploaded.

1. **Create a `.gitignore` file** in your project folder:
   ```bash
   # Create .gitignore and add sensitive files
   echo ".env" >> .gitignore
   echo "venv/" >> .gitignore
   echo "__pycache__/" >> .gitignore
   echo ".streamlit/" >> .gitignore
   ```

2. **Initialize Git and Commit**:
   Open your terminal in the project folder and run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AI Hari Raya Greeting Generator"
   ```

3. **Push to GitHub**:
   - Create a **new repository** on GitHub (it can be Public or Private).
   - Link your local repo and push:
     ```bash
     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
     git branch -M main
     git push -u origin main
     ```

---

## ☁️ Step 2: Deploy to Streamlit Cloud
1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Click the **"Create app"** button.
3. Select your repository, the `main` branch, and set the main file path to `app.py`.
4. Click **"Deploy!"**.

---

## 🔑 Step 3: Configure Your API Key (Secrets)
Your app will fail at first because it won't find the `.env` file. You must add the API key to Streamlit's secure vault.

1. On your Streamlit Dashboard, find your app and click the **three dots (⋮)** > **Settings**.
2. Go to the **Secrets** tab on the left.
3. Paste your API key in **TOML format**:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
4. Click **Save**. The app will automatically reboot and should now work!

---

## ✅ Step 4: Share!
- Once the app is running, copy the URL from your browser (e.g., `https://raya-greeting.streamlit.app`).
- Send the link to your friends and family!

---

## ⚠️ Security Reminders
*   **Never** remove `.env` from your `.gitignore`.
*   **Never** hardcode your API key directly into `app.py`.
*   If you accidentally push your API key to GitHub, **delete it immediately** from the Google AI Studio dashboard and generate a new one.

---
*Created with ❤️ for Hari Raya Aidilfitri*
