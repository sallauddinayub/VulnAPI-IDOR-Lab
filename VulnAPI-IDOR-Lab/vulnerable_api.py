from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB = "users.db"

def get_user(user_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, name, email, balance FROM users WHERE id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2], "balance": row[3]}
    return None


@app.route("/")
def home():
    return "VulnAPI running. Try /user/1"

# ❗ Vulnerable endpoint: no authentication/authorization check (IDOR)
@app.route("/user/<int:user_id>", methods=["GET"])
def user_profile(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    print("Starting vulnerable API at http://127.0.0.1:5000")
    app.run(debug=True)
