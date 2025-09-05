from flask import Flask, jsonify, request, session, render_template
from flask_cors import CORS

app = Flask(__name__)  # APP tanımı en başta
CORS(app)
app.secret_key = "secret123"

# Ana sayfa
@app.route("/")
def home():
    return "Flask çalışıyor 🚀"

# HTML arayüz
@app.route("/shop")
def shop():
    return render_template("index.html", products=products)


# Basit ürün listesi
products = [
    {"id": 1, "name": "4 oz Karton Bardak", "price": 700, "image": "images/bardak1.jpg"},
    {"id": 2, "name": "6.5 oz Karton Bardak", "price": 800, "image": "images/bardak2.jpg"},
    {"id": 3, "name": "7 oz Karton Bardak", "price": 900, "image": "images/bardak3.jpg"},
    {"id": 4, "name": "Özel Baskı Bardak", "price": 2000, "image": "images/bardak4.jpg"}
]

@app.route("/api/products")
def get_products():
    return jsonify(products)

# Basit sepet sistemi
@app.route("/api/cart", methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        item = request.json  # {"id":1, "quantity":2}
        session["cart"].append(item)
        return jsonify({"message": "Ürün eklendi", "cart": session["cart"]})

    return jsonify(session["cart"])

# Hello endpoint
@app.route("/api/hello")
def hello():
    return jsonify(message="Merhaba from Flask!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


    
