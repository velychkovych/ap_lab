from database.models import user

from database.dbUtils import *

from database.schemas import UserSchema


@app.route('/user', methods=["GET"])
def get_users():
    return get_entries(UserSchema, user)


@db_lifecycle
@app.route('/user/<string:username>', methods=["GET"])
def get_user_by_username(username):
    temp_user = session.query(user).filter_by(username=username).first()
    return jsonify(UserSchema().dump(temp_user))


@app.route('/user', methods=["POST"])
def set_user():
    return create_entry(UserSchema, user)


@app.route('/user/<int:idUser>', methods=["PUT"])
def update_user(id):
    return update_entry(UserSchema, user, id)
# @app.route('/user/<int:id>', methods=["DELETE"])
# def del_user(id):
#     return del_entry_by_id(UserSchema, user, id)
