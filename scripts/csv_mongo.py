import pandas as pd
from pymongo import MongoClient

# MongoDB Atlas connection string
uri = "mongodb+srv://AdminDianaD:AdminPassword123!!!@inventory-cluster.9bcqnbb.mongodb.net/?appName=inventory-cluster"

def connect_to_mongodb():
    client = MongoClient(uri)
    db = client["inventory"]
    collection = db["products"]
    return collection


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def convert_to_json(df):
    return df.to_dict(orient="records")


def insert_data(collection, data):

    collection.delete_many({})

    result = collection.insert_many(data)

    print(f"{len(result.inserted_ids)} products inserted successfully.")


def main():

    print("Starting CSV import...")

    collection = connect_to_mongodb()

    df = load_csv("../products.csv")

    json_data = convert_to_json(df)

    insert_data(collection, json_data)

    print("Import complete.")


if __name__ == "__main__":
    main()