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
        self.user_idUser = '10'
        self.user_username = "default"
        self.user_firstname = "default"
        self.user_lastname = "default"
        self.user_password = "default"
        self.user_email = "default"
        self.user_date = "2021-12-08 19:17:01"
        self.user_idUserStatus = "2"

        self.user_auth = self.user_username, self.user_password
        self.admin_auth = '1', '1'
        self.user_firstname = "Example"
        self.not_admin_auth = '2', '2'

        self.user_data = {"idUser": self.user_idUser, "username": self.user_username, "firstname": self.user_firstname, "lastname": self.user_lastname,
                          "password": self.user_password, "email": self.user_email, "idUserStatus": self.user_idUserStatus, "dateOfRegistration": self.user_date, }
        self.user_data_ch = {"idUser": self.user_idUser, "username": self.user_username, "firstname": "user_firstname", "lastname": self.user_lastname,
                          "password": self.user_password, "email": self.user_email, "idUserStatus": self.user_idUserStatus, "dateOfRegistration": self.user_date, }

        self.header = {"Content-Type": "application/json", }

    def test1_post_user(self):
        resp = requests.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(200, resp.status_code)
        self.assertGreaterEqual(resp.json().items(), dict(username="default").items())

    def test2_failed_post_user(self):
        resp = self.client.post("http://localhost:5000/user", headers=self.header, data=json.dumps(self.user_data))
        self.assertEqual(400, resp.status_code)
        self.assertEqual(resp.json, {'message': 'Duplicate entry'})
        self.assertEqual(resp.data, b'{"message":"Duplicate entry"}\n')

    def test3_put_user(self):
        resp = self.client.put("http://localhost:5000/user/" + self.user_idUser, headers=self.header, data=json.dumps(self.user_data_ch), auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test4_put_user(self):
        resp = self.client.put("http://localhost:5000/user/" + self.user_idUser, headers=self.header, data=json.dumps(self.user_data_ch), auth=self.not_admin_auth)
        self.assertEqual(200, resp.status_code)

    def test5_get_user(self):
        resp = self.client.get("http://localhost:5000/user/" + self.user_username, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test6_failed_delete_user(self):
        resp = self.client.delete("http://localhost:5000/user/" + self.user_username, headers=self.header, auth=self.not_admin_auth)
        self.assertEqual(200, resp.status_code)

    def test7_delete_user(self):
        resp = self.client.delete("http://localhost:5000/user/" + self.user_username, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test8_delete_user_failed_2(self):
        resp = self.client.delete("http://localhost:5000/user/" + self.user_username, headers=self.header, auth=self.admin_auth)
        self.assertEqual(404, resp.status_code)


