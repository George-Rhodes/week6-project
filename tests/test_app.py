import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Routine, Excer



class TestBase(TestCase):
    def create_app(self):
    
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
           SECRET_KEY='Cheek_test_key', 
           DEBUG=True)
        return app


    def setUp(self):


        db.create_all()


        route = Routine(rTitle='big muscle work out', author= 'patrick', description='just getting these muscle prestine')
        ex = Excer(routine_id = 1, set_name='lateral pull down', level_num = 35, level_type = 'Kg', set_length = 4, set_type = 'sets')

        db.session.add(route)
        db.session.commit
        db.session.add(ex)
        db.session.commit()




    def tearDown(self):



        db.session.remove()
        db.drop_all()





class Testpages(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code,200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', idNum=1))
        self.assertEqual(response.status_code,200)

    
    def test_view_get(self):
        response = self.client.get(url_for('routine', idNum=1))
        self.assertEqual(response.status_code,200)
    
    def test_addsession_get(self):
        response = self.client.get(url_for('addexcer', idNum=1))
        self.assertEqual(response.status_code,200)

    def test_updatesession_get(self):
        response = self.client.get(url_for('updateEx', idNum=1))
        self.assertEqual(response.status_code,200)
    
    
    def test_delete_get(self):
        response = self.client.get(url_for('deleteEx', idNum=1))
        self.assertEqual(response.status_code,302)


    def test_delete_get(self):
        response = self.client.get(url_for('delete', idNum=1))
        self.assertEqual(response.status_code,302)

    
    
    
    