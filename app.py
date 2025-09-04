from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Frontend başka bir domainden çağırabilsin diye

@app.route("/")
def home():
    return "Flask çalışıyor 🚀"

@app.route("/api/hello")
def hello():
    return jsonify(message="Merhaba from Flask!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
