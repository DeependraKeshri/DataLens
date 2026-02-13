from flask import Flask, render_template, request, jsonify
import random, string, re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/email")
def email():
    return render_template("email.html")

@app.route("/password")
def password():
    return render_template("password.html")

@app.route("/templates")
def templates():
    return render_template("templates.html")

# ---------------- EMAIL ----------------
@app.route("/check-email", methods=["POST"])
def check_email():
    email = request.json["email"]
    score = 0
    missing = []

    if len(email) >= 10: score += 1
    else: missing.append("Increase length")

    if re.search(r"\d", email): score += 1
    else: missing.append("Add numbers")

    if re.search(r"[._]", email): score += 1
    else: missing.append("Add special characters")

    strength = "Strong" if score == 3 else "Medium" if score == 2 else "Weak"
    return jsonify({"strength": strength, "missing": missing})

@app.route("/generate-email", methods=["POST"])
def generate_email():
    keyword = request.json["keyword"]
    result = []
    for _ in range(5):
        result.append(f"{random.choice(['real','pro','official'])}{keyword}{random.randint(10,999)}@gmail.com")
    return jsonify(result)

# ---------------- PASSWORD ----------------
@app.route("/generate-password", methods=["POST"])
def generate_password():
    length = int(request.json["length"])
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return jsonify("".join(random.choice(chars) for _ in range(length)))

@app.route("/check-password", methods=["POST"])
def check_password():
    pwd = request.json["password"]
    missing = []
    if len(pwd) < 8: missing.append("Length < 8")
    if not re.search(r"[A-Z]", pwd): missing.append("Uppercase")
    if not re.search(r"\d", pwd): missing.append("Number")
    if not re.search(r"[!@#$%^&*]", pwd): missing.append("Symbol")
    return jsonify({"status": "Strong" if not missing else "Weak", "missing": missing})

if __name__ == "__main__":
    app.run(debug=True)
