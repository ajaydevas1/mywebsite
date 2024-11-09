from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample user data for login
users = {"user1": "password123", "admin": "adminpass"}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the username and password match
    if username in users and users[username] == password:
        # Redirect to a new page after successful login
        return redirect(url_for('dashboard'))
    else:
        # Stay on the same page and show an error message if login fails
        return "Invalid credentials. Please try again.", 401

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the Dashboard</h1>"

if __name__ == "__main__":
    app.run(debug=True)
