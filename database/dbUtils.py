from functools import wraps

import marshmallow
import sqlalchemy
from flask import jsonify, request

from database.flask_ini import app
from database.models import Session

session = Session()


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
            else:
                return jsonify({'message': str(e), 'type': 'InternalServerError'}), 500

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
    users = model.query.all()
    return jsonify(schema(many=True).dump(users))


@db_lifecycle
def get_entry_by_id(schema, model, id):
    user = session.query(model).get(id)
    return jsonify(schema().dump(user))


@db_lifecycle
@session_lifecycle
def del_entry_by_id(schema, model, id):
    user = session.query(model).get(id)

    if user is None:
        raise TypeError()

    session.delete(user)
    return jsonify(schema().dump(user))
