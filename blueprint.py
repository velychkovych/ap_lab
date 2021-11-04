import dbUtils
from app import app
from schemas import UserSchema
from models import Session
from models import user
from flask import request, jsonify


def db_lifecycle(func):
    def wrapper():
        with Session() as s:
            rez = func(session=s)
            s.commit()
            return rez

    return wrapper



@app.route("/user/signup", methods=["POST"])
@db_lifecycle
def create_user(session):
    user_data = UserSchema().load(request.get_json())
    user_obj = dbUtils.create_entry(user, **user_data)
    session.add(user_obj)

    return jsonify(UserSchema().dump(user_obj))


@app.route("/user", methods=["GET"])
def get_users():
    users = user.query.all()
    return jsonify(UserSchema(many=True).dumps(users))


# @app.route("/user/<int:user_id>")
# def get_user_by_Id(user_id):
#     user_obj = dbUtils.get_entry_by_uid(user, user_id)
#     return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<string:username>")
def get_user_by_Id(username):
    user_obj = dbUtils.get_entry_by_username(user, username)
    return jsonify(UserSchema().dump(user_obj))

if __name__ == '__main__':
    app.run(debug=True)