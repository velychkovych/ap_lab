from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime

engine = create_engine('mysql+pymysql://root:00000000password@localhost:3306/swagger_service')
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class userStatus(BaseModel):
    __tablename__ = "userStatus"

    idUserStatus = Column(Integer, primary_key=True)
    status = Column(VARCHAR(45), nullable=False)


class user(BaseModel):
    __tablename__ = "user"

    idUser = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45), nullable=False)
    firstname = Column(VARCHAR(45), nullable=False)
    lastname = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    dateOfRegistration = Column(DateTime, nullable=False)
    idUserStatus = Column(Integer, ForeignKey(userStatus.idUserStatus))

    def str(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n"


class article(BaseModel):
    __tablename__ = "article"

    idArticle = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    header = Column(VARCHAR(45), nullable=False)
    textOfArticle = Column(VARCHAR(2000), nullable=False)
    idAuthor = Column(Integer, ForeignKey(user.idUser))


class modification(BaseModel):
    __tablename__ = "modification"

    idModification = Column(Integer, primary_key=True)
    dateOfModification = Column(DateTime, nullable=False)
    idUser = Column(Integer, ForeignKey(user.idUser))
    idArticle = Column(Integer, ForeignKey(article.idArticle))
