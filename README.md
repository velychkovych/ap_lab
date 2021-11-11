Щоб запустити проект на своєму пк потрібно:

1. Клонувати проект собі на пк.
2. Встановити віртуальне середовище командою python3.7 -m venv <назва віртуального середовища>
3. Активувати віртуальне середовище source <назва віртуального середовища>/bin/activate
4. Встановити всі залежності, що вказані у файлі requirements.txt.
5. Встановити gunicorn на віртуальне середовище.
6. Запустити WSGI сервер командою gunicorn --bind 0.0.0.0:8000 app:app. Lab_5

alembic downgrade -1


> curl -X GET http://localhost:5000/user
> user
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"firstname\": \"Taras\", \"username\":\"macao\", \"lastname\":\"Vovk\", \"email\":\"adddssdss@asd\",\"password\":\"asdf\"}" http://localhost:5000/user
> curl -X GET http://localhost:5000/user
> curl -X GET http://localhost:5000/user/macao
> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"firstname\": \"Taras\"}" http://localhost:5000/user/1
> curl -X DELETE http://localhost:5000/user/macao
> article
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"header\":\"ads\",\"textOfArticle\":\"aboba\",\"idAuthor\":\"1\"}" http://localhost:5000/article
> curl -X GET http://localhost:5000/article
> curl -X GET http://localhost:5000/article/1
> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"idArticle\": \"1\"}" http://localhost:5000/article/1
> curl -X DELETE http://localhost:5000/article/1
> modification:
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"idUser\":\"1\",\"idArticle\":\"4\"}" http://localhost:5000/article/modification
> curl -X GET http://localhost:5000/article/modification
> curl -X GET http://localhost:5000/article/modification/1
> curl -X GET http://localhost:5000/modification/1
> curl -X DELETE  http://localhost:5000/article/modification/1
