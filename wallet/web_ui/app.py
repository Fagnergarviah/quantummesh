from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/balance/<address>")
def get_balance(address: str):
    return {"balance": 1000, "address": address}
