from flask import Flask, jsonify
from database import init_db
from services.UserServices import register_new_user
from repositories.UserRepository import get_all_users, get_user, att_user, del_user

app = Flask(__name__)

init_db(app)

@app.route("/add")
def add():
    new_user = register_new_user('Alice', 'alice@example.com')

    return jsonify(new_user.to_dict())
    
@app.route("/ver")
def ver():
    users = get_all_users()

    users_json = [user.to_dict() for user in users]
    return jsonify(users_json)

@app.route("/att/<id>/<nome>/<email>")
def att(id, nome, email):
    user = att_user(1, nome, email)

    return jsonify(user.to_dict())

@app.route("/del/<id>")
def dele(id):
    user = del_user(id)

    return jsonify(user.to_dict())

if __name__ == "__main__":
    app.run(debug = True)