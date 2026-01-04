# Code Warlock Portfolio
> A Hybrid Django + FastAPI Architecture

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-005571?style=flat&logo=fastapi)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC?style=flat&logo=tailwind-css)

**Code Warlock** is a next-generation personal portfolio built to demonstrate full-stack mastery. Unlike standard static sites, this project runs a dual-server architecture: a robust **Django** core for the CMS and frontend, paired with a high-performance **FastAPI** microservice for live data fetching.

## Key Features

### 1. Hybrid Backend Core
* **Django (Port 8000):** Handles the Admin Panel, SQL Database, HTML rendering, and static assets.
* **FastAPI (Port 8001):** A dedicated microservice that serves resume data via high-speed JSON endpoints.

### 2. "The Lab" Terminal
* An interactive terminal UI built into the homepage.
* Uses JavaScript to fetch live data from the FastAPI microservice (`/api/profile`, `/api/resume`), simulating a real hacker environment.

### 3. Dynamic PDF Generator
* **Automated CVs:** Never manually update a resume again.
* Uses `xhtml2pdf` to generate a downloadable PDF on-the-fly based on the latest data entered in the Django Admin.

### 4. Code Warlock UI
* Custom **Dark/Neon Mode** toggle.
* Responsive "Glassmorphism" design using **Tailwind CSS**.
* Custom 404 "System Failure" glitch page.

---

## 🛠️ Local Setup

To run this laboratory on your local machine:

### 1. Clone the Repo
```bash
git clone [https://github.com/YOUR_USERNAME/code-warlock.git](https://github.com/YOUR_USERNAME/code-warlock.git)
cd code-warlock

