from flask_testing import TestCase
from Database.flask_ini import db
from app import app
from flask import json


class MyTest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()

import requests


class TestUser(MyTest):

    def setUp(self):
        self.user_username = "s1"
        self.user_password = "dsdasdda"
        self.user_email = "dsada"
        self.user_auth = self.user_username, self.user_password
        self.user_firstname = "Example"

        self.user_data = {"username": self.user_username, "password": self.user_password, "email": self.user_email, }
        self.header = {"Content-Type": "application/json", }

    def test11_post_user(self):
        resp = requests.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(200, resp.status_code)
        self.assertGreaterEqual(resp.json().items(), dict(username="default").items())

    def test22_failed_post_user(self):
        resp = self.client.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(400, resp.status_code)

        self.assertEqual(resp.json, {'message': 'Duplicate entry'})
        self.assertEqual(resp.data, b'{"message":"Duplicate entry"}\n')