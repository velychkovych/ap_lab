Щоб запустити проект на своєму пк потрібно:
1. Клонувати проект собі на пк.
2. Встановити віртуальне середовище командою python3.7 -m venv <назва віртуального середовища>
3. Активувати віртуальне середовище source <назва віртуального середовища>/bin/activate
4. Встановити всі залежності, що вказані у файлі requirements.txt.
5. Встановити gunicorn на віртуальне середовище.
6. Запустити WSGI сервер командою gunicorn --bind 0.0.0.0:8000 app:app.
Lab_7

alembic downgrade -1


> curl -X GET http://localhost:5000/user
> 
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Max\", \"password\": \"ax\"}" http://localhost:5000/user
> 
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Max\", \"email\": \"mx@gmail.com\", \"password\": \"dfghkgh\"}" http://localhost:5000/user
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Max\", \"phone\": \"88005553535\", \"last_name\": \"Last_name\", \"username\": \"fayon\", \"email\": \"mx@gmail.com\", \"password\": \"dfghkgh\"}" http://localhost:5000/user
> 
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"email\": \"mx@gmail.com\", \"password\": \"dfghkgh\"}" http://localhost:5000/user/login
> 
> curl -X GET http://localhost:5000/user/1
>
> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"first_name\": \"pussyBoy\"}" http://localhost:5000/user/2
> 
> curl -X DELETE http://localhost:5000/user/1
> 
> modification:
>
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"firstname\": \"Max\", \"password\": \"ax\"}" http://localhost:5000/user
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"header\":\"ads\",\"textOfArticle\":\"aboba\",\"idAuthor\":\"1\"}" http://localhost:5000/article
> curl -X POST -H "Content-Type:application/json" --data-binary "{\"idUser\":\"1\",\"idArticle\:\"\"}" http://localhost:5000/article/modification
