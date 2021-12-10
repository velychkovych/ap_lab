from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime
import datetime
from Database.flask_ini import db

#engine = create_engine('mysql+pymysql://root:00000000password@localhost:3306/swagger_service')
#engine.connect()

#SessionFactory = sessionmaker(bind=engine)

#Session = scoped_session(SessionFactory)

#BaseModel = declarative_base()
#BaseModel.query = Session.query_property()


class userStatus(db.Model):
    __tablename__ = "userStatus"

    idUserStatus = Column(Integer, primary_key=True)
    status = Column(VARCHAR(45))

    def __init__(self, status):
        self.status = status


class user(db.Model):
    __tablename__ = "user"

    idUser = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45), unique=True)
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45), unique=True)
    password = Column(VARCHAR(100))
    dateOfRegistration = Column(DateTime, default=datetime.datetime.utcnow())
    idUserStatus = Column(Integer, ForeignKey(userStatus.idUserStatus, ondelete='CASCADE'))

    def str(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n"


class article(db.Model):
    __tablename__ = "article"

    idArticle = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow())
    header = Column(VARCHAR(45))
    textOfArticle = Column(VARCHAR(2000))
    idAuthor = Column(Integer, ForeignKey(user.idUser, ondelete='CASCADE'))


class modification(db.Model):
    __tablename__ = "modification"

    idModification = Column(Integer, primary_key=True)
    dateOfModification = Column(DateTime, default=datetime.datetime.utcnow())
    idUser = Column(Integer, ForeignKey(user.idUser, ondelete='CASCADE'))
    idArticle = Column(Integer, ForeignKey(article.idArticle, ondelete='CASCADE'))

    def __init__(self, idUser, idArticle):
        self.idUser = idUser
        self.idArticle = idArticle
