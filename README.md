# 🚀 KIET Bootcamp Feedback Dashboard

A full-stack web application designed to display feedback and details for 550+ students from the KIET Bootcamp. This project connects a **Python Flask** backend with a **Neon PostgreSQL** cloud database to serve real-time data into a clean, responsive frontend.

---

## 🌟 What This Project Does
This dashboard acts as a digital yearbook and feedback tracker. It allows administrators and mentors to:
* **Browse Student Data:** View names, roll numbers, and feedback for hundreds of students.
* **Smart Pagination:** Efficiently loads data 10 students at a time so the app remains lightning-fast.
* **Dynamic Photos:** Pulls student images directly from a GitHub repository (acting as a CDN).
* **Smart Fallbacks:** If a student's photo is missing, it automatically generates a colorful avatar with their initials.

---

## 🛠️ Tech Stack
I built this using a modern, serverless-ready stack:
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API).
* **Backend:** Python (Flask).
* **Database:** PostgreSQL (hosted on Neon.tech).
* **Deployment:** Vercel.
* **Image Hosting:** GitHub Raw Content (CDN).

---

## 💡 The Journey
Building this project was a massive learning experience in full-stack development.
* **Data Cleaning:** I started with raw Excel data, cleaned it using Python's `pandas` library, and converted it to CSV.
* **Database Management:** I learned how to create SQL tables and wrote a custom script to batch-upload 550 records into the cloud.
* **Problem Solving:** I overcame challenges with Linux file systems (WSL), database connection strings, and linking external image assets to build a robust application.

---

## 🚀 How to Run Locally
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/kiet-bootcamp-web.git](https://github.com/YOUR_USERNAME/kiet-bootcamp-web.git)
    cd kiet-bootcamp-web
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the Server:**
    ```bash
    python3 api/index.py
    ```
    Visit `http://127.0.0.1:5000` in your browser.

---

### ❤️ Built by Hemasri
*Passionate about Backend Development, Python, and building systems that solve real-world problems.*# Kiet-bootcamp
