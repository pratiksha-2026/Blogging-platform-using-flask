import unittest
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_registration(self):
        hashed_pw = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='testuser', email='test@test.com', password=hashed_pw)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
            user_in_db = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user_in_db)

    def test_login(self):
        # Create a user to log in
        hashed_pw = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='testuser', email='test@test.com', password=hashed_pw)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        
        # Attempt login
        response = self.app.post('/login', data=dict(email='test@test.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Check if login success message or 'Logout' link appears
        self.assertIn(b'Logout', response.data)

if __name__ == '__main__':
    unittest.main()