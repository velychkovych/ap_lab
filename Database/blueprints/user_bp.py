import bcrypt

from database.models import user

from database.dbUtils import *

from database.schemas import UserSchema


@app.route('/user', methods=["POST"])
@db_lifecycle
@session_lifecycle
def set_user():
    data = UserSchema().load(request.get_json())

    password = request.json.get('password', None)
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    data.update({"password": hashed})
    entry = user(**data)
    session.add(entry)
    session.flush()
    return jsonify(UserSchema().dump(entry))


@app.route('/user', methods=["GET"])
def get_users():
    return get_entries(UserSchema, user)


@app.route('/user/<string:username>', methods=["GET"])
def get_user_by_username(username):
    entry = session.query(user).filter_by(username=username).first()
    return jsonify(UserSchema().dump(entry))


@app.route('/user/<int:id>', methods=["PUT"])
def update_user(id):
    return update_entry(UserSchema, user, id)


@app.route('/user/<string:username>', methods=["DELETE"])
@db_lifecycle
@session_lifecycle
def del_user_by_username(username):
    entry = session.query(user).filter_by(username=username).first()

    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)

    session.delete(entry)
    return jsonify(UserSchema().dump(entry))
