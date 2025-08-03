from flask import Blueprint, request, jsonify
from app.services import user_service

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = user_service.get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@user_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user, error = user_service.create_user(data.get("name"), data.get("email"), data.get("password"))
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data.get("name"), data.get("email"))
    if not user:
        return jsonify({"error": "Update failed"}), 400
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not user_service.delete_user(user_id):
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200
