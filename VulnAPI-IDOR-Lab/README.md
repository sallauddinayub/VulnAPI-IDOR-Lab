# VulnAPI — IDOR Vulnerability Testing Lab

This project demonstrates an **Insecure Direct Object Reference (IDOR)** vulnerability using a vulnerable REST API and an automated exploitation script.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Initialize database:
```
python init_db.py
```

3. Start the vulnerable API:
```
python vulnerable_api.py
```

4. In another terminal, run the exploit:
```
python exploit_idor.py
```

You will see exposed user records if the vulnerability is present.
