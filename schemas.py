from marshmallow import Schema, fields

class UserSchema(Schema):
    idUser = fields.Integer()
    firstname = fields.String()
    username = fields.String()
