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


class TestArticle(MyTest):

    def setUp(self):
        self.modification_idModification = '17'
        self.modification_idUser = "14"
        self.modification_idArticle = "11"

        self.admin_auth = '1', '1'
        self.not_admin_auth = '2', '2'

        self.modification_data_ch = {"idUser": "21", "idArticle": self.modification_idArticle, }

        self.header = {"Content-Type": "application/json", }

    def test1_get_modification(self):
        resp = self.client.get("http://localhost:5000/article/modification", headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test2_get_modifications(self):
        resp = self.client.get("http://localhost:5000/article/modification/" + self.modification_idArticle, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test3_get_modifications_failed(self):
        resp = self.client.get("http://localhost:5000/article/modification/" + self.modification_idArticle, headers=self.header, auth=self.not_admin_auth)
        self.assertEqual(200, resp.status_code)

    def test4_get_modifications(self):
        resp = self.client.get("http://localhost:5000/modification/" + self.modification_idModification, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test5_get_modifications_failed(self):
        resp = self.client.get("http://localhost:5000/modification/" + self.modification_idModification, headers=self.header, auth=self.not_admin_auth)
        self.assertEqual(200, resp.status_code)

    def test6_delete_modifications_failed(self):
        resp = self.client.delete("http://localhost:5000/article/modification/" + self.modification_idModification, headers=self.header, auth=self.not_admin_auth)
        self.assertEqual(200, resp.status_code)