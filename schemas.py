from marshmallow import post_load, Schema, fields
from models import user


class UserSchema(Schema):
    idUser = fields.Integer()
    firstname = fields.String()
