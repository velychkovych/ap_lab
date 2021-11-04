from lab_6 import Session, user, userStatus, article, modification
from datetime import datetime

userstatus1 = userStatus(status='superuser')
user1 = user(username='user1', firstname='name1user', lastname='surname1user', email='user1@email.com',
             password='passwordUser1', dateOfRegistration=datetime.now(), idUserStatus=userstatus1.idUserStatus)
article1 = article(date=datetime.now(), header='article1',
                   textOfArticle='someText1', idAuthor=1)
modification1 = modification(
    dateOfModification=datetime.now(), idUser=1, idArticle=1)


with Session() as session:
    session.add(user1)
    session.commit()
    session.add(userstatus1)
    session.commit()
    session.add(article1)
    session.commit()
    session.add(modification1)
    session.commit()
    
print(session.query(user).all()[0])
