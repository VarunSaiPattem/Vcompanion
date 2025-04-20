from flask import Flask, jsonify, render_template
from scraper import login_vtop

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify(login_vtop())

if __name__ == "__main__":
    app.run(debug=True)