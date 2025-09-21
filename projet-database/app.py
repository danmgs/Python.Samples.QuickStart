from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# 🔹 Connexion MongoDB (par défaut sur localhost)
client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
users_collection = db["users"]

# Utilitaire : convertir ObjectId en string
def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

# CREATE (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    result = users_collection.insert_one(new_user)
    return jsonify({"id": str(result.inserted_id)}), 201

# READ (GET all)
@app.route("/users", methods=["GET"])
def get_users():
    users = [serialize_user(u) for u in users_collection.find()]
    return jsonify(users), 200

# READ (GET by id)
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(serialize_user(user)), 200
    return jsonify({"error": "User not found"}), 404

# UPDATE (PUT)
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    updated_user = {"$set": {
        "name": data.get("name"),
        "email": data.get("email")
    }}
    result = users_collection.update_one({"_id": ObjectId(id)}, updated_user)
    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated"}), 200

# DELETE
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = users_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
