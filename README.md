# Salary Slip Server - Local Setup Guide

## Step 1: Prerequisites
Ensure you have the following installed on your system:
- **Python (3.x recommended)** → [Download Python](https://www.python.org/downloads/)
- **Git** → [Download Git](https://git-scm.com/downloads)

---

## Step 2: Clone the Repository
Open a terminal or command prompt and run:
```sh
git clone https://github.com/Kjaish/salary_slip_server.git
cd salary_slip_server
```

---

## Step 3: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv  # Creates a virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

---

## Step 4: Install Dependencies
Check if a `requirements.txt` file is available. If it exists, install dependencies with:
```sh
pip install -r requirements.txt
```
If `requirements.txt` is missing, you may need to manually install common Flask-related libraries like:
```sh
pip install flask pandas reportlab
```

---

## Step 5: Set Up Environment Variables (If Required)
Check if the project requires any `.env` file. If an `.env.example` file is provided, create a `.env` file and configure it.
```sh
cp .env.example .env
```
Then update `.env` with the necessary details.

---

## Step 6: Run the Application
Start the Flask server with:
```sh
python app.py
```
or (if using Flask's built-in CLI):
```sh
flask run
```

---

## Step 7: Access the Application
Once running, the app should be accessible at:
```sh
http://127.0.0.1:5000
```
or
```sh
http://localhost:5000
```
(Port may vary based on the configuration)

---

## Step 8: Testing the API (If applicable)
Use **Postman** or **cURL** to test API endpoints if this is a backend service.
