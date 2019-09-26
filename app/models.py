from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#User class
# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     pass_secure = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String(100))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    profile_pic_path = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'author', lazy = True) 
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    def ___repr__():
        return f"User ('{self.username}', '{self.email}'')"
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comments', backref = 'author' , lazy = True)
    
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    
    
    def ___repr__():
        return f"Blog ('{self.title}', '{self.date_posted}'')"
    

class Comments(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    comment = db.column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
        
    def ___repr__(self):
        return f"Comments('{self.comment}')"
        