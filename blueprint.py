import dbUtils
from app import app
from schemas import UserSchema
from models import Session
from models import user
from flask import request, jsonify

# def db_lifecycle(func):
#     def wrapper():
#         print("fsg")
#         func()

#     return wrapper
#     # with Session as session:


@app.route("/user", methods=["POST"])
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = dbUtils.create_entry(user, **user_data)

    # first_name = request.json['first_name']
    # user_obj = user(first_name=first_name)
    # print(user_obj)

    with Session() as s:
        s.add(user_obj)
        s.commit()

    return UserSchema().dump(user_data)
    # return "",200


if __name__ == '__main__':
    app.run(debug=True)
