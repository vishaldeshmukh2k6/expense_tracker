from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/add")
def add_transaction():
    return render_template("add_transaction.html")

@app.route("/logout")
def logout():
    return "Logged out (dummy page)"
