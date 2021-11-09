from database.models import user

from database.dbUtils import *

from database.schemas import UserSchema


@app.route('/user', methods=["GET"])
def get_users():
    return get_entries(UserSchema, user)


@app.route('/user', methods=["POST"])
def set_user():
    return create_entry(UserSchema, user)


# @app.route('/user/<int:id>', methods=["DELETE"])
# def del_user(id):
#     return del_entry_by_id(UserSchema, user, id)
