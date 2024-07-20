from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['property_db']
collection = db['properties']

properties = [
    {
        "full_address": "123 Main St, Springfield, IL 62701",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_footage": 1500,
        "price": 250000,
        "description": "A lovely single-family home in the heart of Springfield."
    },
    {
        "full_address": "456 Elm St, Shelbyville, IL 62565",
        "bedrooms": 4,
        "bathrooms": 3,
        "square_footage": 2000,
        "price": 350000,
        "description": "Spacious home with a modern kitchen and large backyard."
    },
]

collection.insert_many(properties)

print("Property data inserted successfully.")
