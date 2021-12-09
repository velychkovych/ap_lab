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
        self.article_idArticle = '10'
        self.article_date = "2021-12-08"
        self.article_header = "default"
        self.article_textOfArticle = "default"
        self.article_idAuthor = "14"

        self.admin_auth = '1', '1'
        self.not_admin_auth = '2', '2'

        self.article_data = {"idArticle": self.article_idArticle, "date": self.article_date, "header": self.article_header,
                          "textOfArticle": self.article_textOfArticle, "idAuthor": self.article_idAuthor, }
        self.article_data_ch = {"idArticle": self.article_idArticle, "date": self.article_date,  "header": self.article_header,
                          "textOfArticle": self.article_textOfArticle, "idAuthor": self.article_idAuthor, }

        self.header = {"Content-Type": "application/json", }

    def test1_post_article(self):
        resp = self.client.post("http://localhost:5000/article", headers=self.header, data=json.dumps(self.article_data), auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test2_get_article(self):
        resp = self.client.get("http://localhost:5000/article/" + self.article_idArticle, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test3_get_articles(self):
        resp = self.client.get("http://localhost:5000/article", headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test4_put_article(self):
        resp = self.client.put("http://localhost:5000/article/" + self.article_idArticle, headers=self.header, data=json.dumps(self.article_data_ch), auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test5_delete_article(self):
        resp = self.client.delete("http://localhost:5000/article/" + self.article_idArticle, headers=self.header, auth=self.admin_auth)
        self.assertEqual(200, resp.status_code)

    def test6_put_article_failed(self):
        resp = self.client.put("http://localhost:5000/article/" + self.article_idArticle, headers=self.header,
                               data=json.dumps(self.article_data_ch), auth=self.admin_auth)
        self.assertEqual(404, resp.status_code)
