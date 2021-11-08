from database.models import user

from database.dbUtils import *

from database.schemas import UserSchema


@app.route('/user', methods=["GET"])
def get_users():
    return get_entries(UserSchema, user)


@app.route('/user', methods=["DELETE"])
def del_user(id):
    return del_entry_by_id(schema, model, id)
