import unittest
from server import create_test_app
from models import *
from database import delete_db




class TestsOfSoftwareEng(unittest.TestCase):

    # test setup -> executes before each test
    def setUp(self):
        self.app = create_test_app()
        self.client = self.app.test_client()


    # test teardown -> executes after each test
    def tearDown(self):
        delete_db()
        self.app.db.drop_all()

    def set_admin_creation(self):
        data = dict(username='firstTry',email='firstTry@gmail.com',password='first',passwordAgain='first',appname='firstApp')
        response = self.client.post('/',data=data,follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def set_category(self):
        self.app.db.session.add(Categories('MEN','No description'))
        self.app.db.session.commit()

    def set_model(self):
        self.app.db.session.add(Actors('model1','model2','model1@gmail.com',True,'boy',20,123123123123))
        self.app.db.session.commit()
        actor = Actors.query.filter_by(email='model1@gmail.com').first()
        self.app.db.session.add(ActorBody(actor.id, 180, 90, 'White', 'Black','Curly', 'blue', 90, 60, 90,42))
        self.app.db.session.add(ActorSoul(actor.id, 'facebook', 'twitter', 'instagram', 'no description'))
        category_id = Categories.query.filter_by(name='MEN').first()
        self.app.db.session.add(ActorModel(actor.id, category_id.id))
        self.app.db.session.add(Photos(user_id=actor.id))
        self.app.db.session.commit()


    def test_application_start(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/home',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_apply_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/apply',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_contact_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/contact',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_contact_post(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        data = dict(name='emre',email='uysalemre02@gmail.com',subject='nothing',message='nothing to do')
        response = self.client.post('/contact',content_type='multipart/form-data',data=data,follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_signup_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/signup',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_signup_post(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        data = dict(username='company',email='componyuser@gmail.com',password='company1',passwordAgain='company1')
        response = self.client.post('/signup',data=data,follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.app.db.session.query(User).filter(User.email == 'componyuser@gmail.com').update({User.active: True})
        self.app.db.session.commit()

    def test_company_login_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/login',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_company_login_post(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        data = dict(email='componyuser@gmail.com',passw='compony1')
        response = self.client.post('/login',data=data,follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_category_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/categories/MEN',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_model_get(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        response = self.client.get('/MEN/1',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_admin_login(self):
        self.set_admin_creation()
        self.set_category()
        self.set_model()
        data = dict(email='firstTry@gmail.com', passw='first')
        response = self.client.post('/admin-login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
