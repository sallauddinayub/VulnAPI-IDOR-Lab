# 🔓 VulnAPI — IDOR Vulnerability Exploitation Lab

VulnAPI is a deliberately vulnerable REST API created to demonstrate an **Insecure Direct Object Reference (IDOR)** vulnerability and its exploitation using an automated Python script.

This project simulates a real-world web application security flaw where an attacker can access other users’ data by manipulating object identifiers in the URL.

---

## 📌 Objective
To understand and demonstrate **Broken Access Control**, which is ranked #1 in the OWASP Top 10 Web Application Security Risks.

---

## 🧠 Vulnerability Explained

The API exposes a user profile endpoint:

/user/<id>


Example:



http://127.0.0.1:5000/user/1


The application directly retrieves data from the database using the provided ID **without verifying authorization**.

Because of this, an attacker can simply change the ID:



/user/1 → Rahul's account
/user/2 → Priya's account
/user/3 → Another user's data


This is called **IDOR (Insecure Direct Object Reference)**.

---

## ⚙️ How the Attack Works

The exploitation script:

1. Iterates through sequential user IDs
2. Sends HTTP GET requests to the API
3. Checks server responses
4. Extracts exposed records

The script automatically enumerates accounts and retrieves sensitive information.

---

## ▶️ How to Run

Install dependencies:



pip install -r requirements.txt


Initialize database:



python init_db.py


Start vulnerable server:



python vulnerable_api.py


Open browser:



http://127.0.0.1:5000/user/1


Run attacker script (new terminal):



python exploit_idor.py


---

## 🔐 Security Impact

An attacker can access:
- user names
- email addresses
- account balances

This demonstrates **Broken Access Control**, a critical security vulnerability that can lead to data leakage.

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite
- REST API Testing
- HTTP Requests

---

## 🧩 How to Fix

The server must verify authorization before returning data.  
Instead of trusting the ID parameter, the application should check whether the authenticated user owns the requested resource.

---

## 👨‍💻 Author
Sallauddin Ayub  
M.Tech Cybersecurity
