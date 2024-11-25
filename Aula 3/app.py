from flask import Flask, request, jsonify
from database import init_db
from repository import UserRepository

app = Flask(__name__)

# Instanciando o repositório
userRepository = UserRepository()

@app.route('/users', methods=['GET'])
def get_users():
    users = userRepository.get_all_users()
    return jsonify([user.toJson() for user in users])

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = userRepository.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')
    new_user = userRepository.create_user(name, email)
    return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    updated_user = userRepository.update_user(user_id, name, email)
    if updated_user:
        return jsonify({'id': updated_user.id, 'name': updated_user.name, 'email': updated_user.email})
    return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_user = userRepository.delete_user(user_id)
    if deleted_user:
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)