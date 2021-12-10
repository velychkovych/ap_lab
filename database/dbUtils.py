from functools import wraps
import sqlalchemy
import marshmallow
from flask import jsonify, request

from Database.flask_ini import app
from Database.flask_ini import db

session = db.session


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def db_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, ValueError):
                return jsonify({'message': e.args[0], 'type': 'ValueError'}), 400
            elif isinstance(e, AttributeError):
                return jsonify({'message': e.args[0], 'type': 'AttributeError'}), 400
            elif isinstance(e, KeyError):
                return jsonify({'message': e.args[0], 'type': 'KeyError'}), 400
            elif isinstance(e, TypeError):
                return jsonify({'message': e.args[0], 'type': 'TypeError'}), 400
            elif isinstance(e, marshmallow.exceptions.ValidationError):
                if str(e.args[0]).find("Unknown field") != -1:
                    raise InvalidUsage("Unknown field", status_code=400)
                elif str(e.args[0]).find("Not a valid") != -1:
                    raise InvalidUsage("Wrong type", status_code=400)
                raise e
            elif isinstance(e, sqlalchemy.exc.IntegrityError):
                if str(e.args[0]).find("Duplicate entry") != -1:
                    raise InvalidUsage("Duplicate entry", status_code=400)
                if str(e.args[0]).find("Cannot delete or update a parent row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot delete or update this object", status_code=400)
                if str(e.args[0]).find("Cannot add or update a child row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot add or update this object, incorrect data", status_code=400)
                else:
                    raise InvalidUsage("Incorrect data", status_code=400)
            else:
                raise e
    return wrapper


def session_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rez = func(*args, **kwargs)
            session.commit()
            return rez
        except Exception as e:
            session.rollback()
            raise e

    return wrapper


@db_lifecycle
@session_lifecycle
def create_entry(schema, model):
    data = schema().load(request.get_json())
    entry = model(**data)
    session.add(entry)
    return jsonify(schema().dump(entry))


@db_lifecycle
def get_entries(schema, model):
    entries = model.query.all()
    return jsonify(schema(many=True).dump(entries))


@db_lifecycle
def get_entry_by_id(schema, model, id):
    entry = session.query(model).get(id)
    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)
    return jsonify(schema().dump(entry))


@db_lifecycle
@session_lifecycle
def del_entry_by_id(schema, model, id):
    entry = session.query(model).get(id)

    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)

    session.delete(entry)
    return jsonify(schema().dump(entry))


@db_lifecycle
@session_lifecycle
def update_entry(schema, model, id):
    data = schema().load(request.get_json())
    entry = session.query(model).get(id)

    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)

    for key, value in data.items():
        setattr(entry, key, value)

    return jsonify(schema().dump(entry))
