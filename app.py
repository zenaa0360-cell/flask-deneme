from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "secret123"

# Ürünler
products = [
    {"id": 1, "name": "4 oz Karton Bardak", "price": 700, "image": "images/bardak1.jpg"},
    {"id": 2, "name": "6.5 oz Karton Bardak", "price": 800, "image": "images/bardak2.jpg"},
    {"id": 3, "name": "7 oz Karton Bardak", "price": 900, "image": "images/bardak3.jpg"},
    {"id": 4, "name": "Özel Baskı Bardak", "price": 2000, "image": "images/bardak4.jpg"}
]

@app.route("/")
def home():
    return "Flask çalışıyor 🚀"

@app.route("/shop")
def shop():
    return render_template("index.html", products=products)

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Sepet sistemi
@app.route("/api/cart", methods=["GET","POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method=="POST":
        item=request.json
        session["cart"].append(item)
        return jsonify({"message":"Ürün eklendi","cart":session["cart"]})
    return jsonify(session["cart"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

