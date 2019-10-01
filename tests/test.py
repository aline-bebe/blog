import unittest
from app.models import User,Blog
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = '1111', username = "ally",email = "ally@gmail.com",profile_pic_path = "/srtatic")

    def test_save_user(self):
        self.new_user.save_user()
       

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
        