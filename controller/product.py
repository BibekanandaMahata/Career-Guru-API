from app import app

@app.route("/product")
def product():
    return "This is the product page."
