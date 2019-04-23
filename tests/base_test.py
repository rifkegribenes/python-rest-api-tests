"""
BaseTest

Parent class to each non-unit test
Dynamic instantiation of database to ensure
blank database on each test run
"""

from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self) -> None:
        # make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self) -> None:
        # database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()

