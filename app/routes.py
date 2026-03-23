from fastapi import APIRouter
from app.database import collection

router = APIRouter()

# Get a single product by ID
@router.get("/getSingleProduct")
def get_single_product(id: int):
    product = collection.find_one({"ProductID": id}, {"_id": 0})
    return product

# Get all products
@router.get("/getAll")
def get_all():
    products = list(collection.find({}, {"_id": 0}))
    return products

# Add new product
from app.models import Product

@router.post("/addNew")
def add_new(product: Product):
    collection.insert_one(product.dict())
    return {"message": "Product added successfully"}

# Delete a product by ID
@router.delete("/deleteOne")
def delete_one(id: int):
    result = collection.delete_one({"ProductID": id})
    return {"deleted": result.deleted_count}

# Products starting with a specific letter
@router.get("/startsWith")
def starts_with(letter: str):
    products = list(collection.find(
        {"Name": {"$regex": f"^{letter}", "$options": "i"}},
        {"_id": 0}
    ))
    return products

# Paginate products by ID range
@router.get("/paginate")
def paginate(start: int, end: int):
    products = list(collection.find(
        {"ProductID": {"$gte": start, "$lte": end}},
        {"_id": 0}
    ).limit(10))
    return products

import requests

# Convert price from USD to EUR
@router.get("/convert")
def convert_price(id: int):
    product = collection.find_one({"ProductID": id})

    if not product:
        return {"error": "Product not found"}

    usd_price = product["UnitPrice"]

    # Exchange rate API
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()

    eur_rate = data["rates"]["EUR"]

    eur_price = usd_price * eur_rate

    return {
        "ProductID": id,
        "PriceUSD": usd_price,
        "PriceEUR": round(eur_price, 2)
    }