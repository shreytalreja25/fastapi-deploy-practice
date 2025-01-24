from fastapi import FastAPI
import json

app = FastAPI()

# Load data from JSON file
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

@app.get("/users")
def get_users():
    data = load_data()
    return data["users"]

@app.get("/products")
def get_products():
    data = load_data()
    return data["products"]

@app.get("/orders")
def get_orders():
    data = load_data()
    return data["orders"]

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    data = load_data()
    user = next((user for user in data["users"] if user["id"] == user_id), None)
    return user or {"error": "User not found"}

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    data = load_data()
    product = next((product for product in data["products"] if product["id"] == product_id), None)
    return product or {"error": "Product not found"}
