from flask import Flask, abort, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe", "email": "john@google.com", "age": 25},
    {"id": 2, "name": "Jane Smith", "email": "jane@msn.com", "age": 30},
    {"id": 3, "name": "Bob Johnson", "email": "bob@hotmail.com", "age": 40},
    {"id": 4, "name": "Jack Edwards", "email": "jak@gmail.com", "age": 40},
    {"id": 5, "name": "Julie Banks", "email": "julie@gmail.com", "age": 40},
]


@app.route("/api/users", methods=["GET"])
def get_users():
    return {"results": users}


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next(filter(lambda u: u.get("id") == user_id, users), None)

    if user is None:
        abort(404)

    return {"user": user}


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    last_user_id = users[-1].get("id")

    new_user = {"id": last_user_id + 1, **data}
    users.append(new_user)

    return {"msg": "User created", "user": new_user}


@app.route("/api/users/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    data = request.json

    user = None
    for i, u in enumerate(users):
        if u.get("id") == user_id:
            users[i] = {**u, **data}
            user = users[i]

    if user is None:
        abort(404)

    return {"msg": "User updated", "user": user}


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = None
    for i, u in enumerate(users):
        if u.get("id") == user_id:
            user = u
            users.pop(i)

    if user is None:
        abort(404)

    return {"msg": "User deleted"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
