from flask import Blueprint, request, jsonify
from backend.config import ADMIN_USERNAME, ADMIN_PASSWORD

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure"}), 401
