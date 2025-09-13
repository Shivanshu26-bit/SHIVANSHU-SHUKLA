from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Alice', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 22}
]

@app.route('/')
def home():
    return "<h1>Welcome to the Simple User Info API</h1>"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Name and age required!'}), 400
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'age': data['age']
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
