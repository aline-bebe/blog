import unittest
from app.models import User,Blog
from app import db

       

class BlogTest(unittest.TestCase):
    def setUp(self):
        
        self.new_blog = Blog(id=2,title='view blog',content="content",date_posted = "12-2-2013"  )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,2)
        self.assertEquals(self.new_blog.title,'view blog')
        self.assertEquals(self.new_blog.date_posted,"12-2-2013")
        

    def test_save_blog(self):
        self.new_blog.save_blog()

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = '1234')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234'))

    
        