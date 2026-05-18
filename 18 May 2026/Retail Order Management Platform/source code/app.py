from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Retail Order Management Platform"

@app.route("/health")
def health():
    return "Order Service Healthy"

@app.route("/order-status")
def order_status():
    return "Order Processing Successfully"

@app.route("/inventory")
def inventory():
    return "Inventory Available"

if __name__ == "__main__":
    app.run()
