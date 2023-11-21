#!/usr/bin/env python3
""" Module of Index views
"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.session_auth import SessionAuth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handle user login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({'error': "email missing"}), 400
    if password is None or password == '':
        return jsonify({'error': "password missing"}), 400
    user = User.search({"email": email})
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404
    if user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    id = auth.create_session(user.id)
    res = jsonify(user.to_json())
    res.set_cookie(os.getenv("SESSION_NAME"), id)
    return res
