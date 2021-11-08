from marshmallow import Schema, fields


class UserSchema(Schema):
    idUser = fields.Integer()
    username = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String()
    password = fields.String()
    dateOfRegistration = fields.Date()


class ArticleSchema(Schema):
    idArticle = fields.Integer()
    date = fields.Date()
    header = fields.String()
    textOfArticle = fields.String()
    idAuthor = fields.Integer()


class ModificationSchema(Schema):
    idModification = fields.Integer()
    dateOfModification = fields.Date()
    idUser = fields.Integer()
    idArticle = fields.Integer()