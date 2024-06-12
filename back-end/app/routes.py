import app.routes
from flask import request, jsonify
from app import app, db
from app.models import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.routes('/home', methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello World"
    })

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 409
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/chatbots', methods=['POST'])
@jwt_required()
def create_chatbot():
    data = request.get_json()
    name = data['name']
    description = data['description']
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()
    new_chatbot = Chatbot(name=name, description=description, user=user)
    db.session.add(new_chatbot)
    db.session.commit()
    return jsonify({"msg": "Chatbot created successfully"}), 201

@app.route('/chatbots', methods=['GET'])
@jwt_required()
def get_chatbots():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()
    chatbots = Chatbot.query.filter_by(user=user).all()
    return jsonify(chatbots=[{"id": c.id, "name": c.name, "description": c.description} for c in chatbots]), 200