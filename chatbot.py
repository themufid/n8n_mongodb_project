from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['property_db']
collection = db['properties']

@app.route('/query', methods=['POST'])
def query_properties():
    query_type = request.json.get('query_type')
    query_value = request.json.get('query_value')
    
    if query_type == "bedrooms":
        results = collection.find({"bedrooms": {"$gte": query_value}})
    elif query_type == "price":
        results = collection.find({"price": {"$lte": query_value}})
    else:
        return jsonify({"error": "Invalid query type"}), 400

    response = []
    for result in results:
        response.append({
            "full_address": result["full_address"],
            "bedrooms": result["bedrooms"],
            "bathrooms": result["bathrooms"],
            "square_footage": result["square_footage"],
            "price": result["price"],
            "description": result["description"]
        })
    
    return jsonify(response)

@app.route('/test_connection', methods=['GET'])
def test_connection():
    try:
        collection.find_one()
        return jsonify({"status": "Connection successful"}), 200
    except Exception as e:
        return jsonify({"status": "Connection failed", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
