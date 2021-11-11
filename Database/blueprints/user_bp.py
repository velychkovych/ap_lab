from database.models import user

from database.dbUtils import *

from database.schemas import UserSchema


@app.route('/user', methods=["POST"])
def set_user():
    return create_entry(UserSchema, user)


@app.route('/user', methods=["GET"])
def get_users():
    return get_entries(UserSchema, user)


@app.route('/user/<string:username>', methods=["GET"])
def get_user_by_username(username):
    entry = session.query(user).filter_by(username=username).first()
    return jsonify(UserSchema().dump(entry))


@app.route('/user/<int:idUser>', methods=["PUT"])
def update_user(id):
    return update_entry(UserSchema, user, id)


@db_lifecycle
@session_lifecycle
@app.route('/user/<string:username>', methods=["DELETE"])
def del_user_by_username(username):
    entry = session.query(user).filter_by(username=username).first()

    if entry is None:
        raise TypeError()

    session.delete(entry)
    return jsonify(UserSchema().dump(entry))
