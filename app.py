from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins (modify origins if needed for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins if needed for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Allow deployment on Render by setting dynamic port
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
