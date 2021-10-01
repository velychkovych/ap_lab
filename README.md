Щоб запустити проект на своєму пк потрібно:
1.Клонувати проект собі на пк.
2.Встановити віртуальне середовище командою python3.7 -m venv <назва віртуального середовища>
3.Активувати віртуальне середовище source <назва віртуального середовища>/bin/activate
4.Встановити всі залежності, що вказані у файлі requirements.txt.
5.Встановити gunicorn на віртуальне середовище.
6.Запустити WSGI сервер командою gunicorn --bind 0.0.0.0:8000 app:app.
