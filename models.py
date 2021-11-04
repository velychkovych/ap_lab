from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime

engine = create_engine('mysql+pymysql://root:pass@localhost:3306/db')
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class userStatus(BaseModel):
    __tablename__ = "userStatus"

    idUserStatus = Column(Integer, primary_key=True)
    status = Column(VARCHAR(45))


class user(BaseModel):
    __tablename__ = "user"

    idUser = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    dateOfRegistration = Column(DateTime)
    idUserStatus = Column(Integer, ForeignKey(userStatus.idUserStatus))

    # def __init__(self, firstname):
    #     self.firstname = firstname

    def str(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n"


class article(BaseModel):
    __tablename__ = "article"

    idArticle = Column(Integer, primary_key=True)
    date = Column(DateTime)
    header = Column(VARCHAR(45))
    textOfArticle = Column(VARCHAR(2000))
    idAuthor = Column(Integer, ForeignKey(user.idUser))


class modification(BaseModel):
    __tablename__ = "modification"

    idModification = Column(Integer, primary_key=True)
    dateOfModification = Column(DateTime)
    idUser = Column(Integer, ForeignKey(user.idUser))
    idArticle = Column(Integer, ForeignKey(article.idArticle))
