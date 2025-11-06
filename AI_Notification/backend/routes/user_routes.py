from flask import Blueprint, jsonify, request
from backend.models.user_model import db, User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email, "role": u.role} for u in users])

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'], phone=data['phone'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"status": "success"}), 201
