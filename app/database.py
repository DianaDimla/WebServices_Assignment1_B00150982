from pymongo import MongoClient

uri = "mongodb+srv://AdminDianaD:AdminPassword123!!!@inventory-cluster.9bcqnbb.mongodb.net/?appName=inventory-cluster"

client = MongoClient(uri)

db = client["inventory"]
collection = db["products"]