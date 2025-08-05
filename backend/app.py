from flask import Flask, request, jsonify, session, redirect, send_from_directory, abort
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from model import predict_url
from utils import extract_features
import os

# ✅ Absolute path to root directory and frontend
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FRONTEND_FOLDER = os.path.join(BASE_DIR, 'frontend')

# ✅ Initialize Flask app with static frontend folder
app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')
CORS(app)
app.secret_key = 'your-secret-key'  # 🚨 Change this before deploying

# 🧠 In-memory user store (replace with database for real app)
users = {}

# ✅ Home route - requires login
@app.route('/')
def home():
    if "user" in session:
        return send_from_directory(app.static_folder, 'index.html')
    return redirect('/login.html')

# ✅ Serve static files like login.html, signup.html, etc.
@app.route('/<path:path>')
def static_file(path):
    full_path = os.path.join(app.static_folder, path)
    if os.path.isfile(full_path):
        return send_from_directory(app.static_folder, path)
    return abort(404)

# ✅ Signup route
@app.route('/signup', methods=["POST"])
def signup():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return "Missing fields", 400

    if email in users:
        return "User already exists", 400

    users[email] = generate_password_hash(password)
    return redirect("/login.html")

# ✅ Login route
@app.route('/login', methods=["POST"])
def login():
    email = request.form.get("username")
    password = request.form.get("password")

    if not email or not password:
        return "Missing credentials", 400

    if email in users and check_password_hash(users[email], password):
        session["user"] = email
        return redirect("/")
    return "Invalid credentials", 401

# ✅ Logout route
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect("/login.html")

# ✅ Optional dashboard
@app.route('/dashboard')
def dashboard():
    if "user" in session:
        return f"""
        <h1>Welcome, {session['user']}!</h1>
        <a href='/'>Go to Homepage</a><br>
        <a href='/logout'>Logout</a>
        """
    return redirect("/login.html")

# ✅ Phishing URL prediction API (with error handling)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        features = extract_features(url)
        result = predict_url(features)
        return jsonify({"url": url, "phishing": int(result)})
    except Exception as e:
        print("❌ Prediction error:", str(e))
        return jsonify({"error": "Prediction failed"}), 500

# ✅ Check current user
@app.route('/user')
def get_user():
    if "user" in session:
        return jsonify({"email": session["user"]})
    return jsonify({"email": None})

# ✅ Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
