from flask_httpauth import HTTPBasicAuth
from database.dbUtils import *
import bcrypt

from database.models import user, userStatus
from database.schemas import UserSchema

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    obj = session.query(user).filter_by(username=username).first()
    if obj and bcrypt.checkpw(password.encode("utf-8"), obj.password.encode("utf-8")):
        return obj
    else:
        return False


def is_admin():
    userstatusid = auth.current_user().idUserStatus
    if session.query(userStatus).filter_by(idUserStatus=userstatusid).first().status == 'superuser':
        return True
    else:
        return False
