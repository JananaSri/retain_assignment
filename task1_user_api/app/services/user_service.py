from app import db
from app.models.user import User
from app.utils.security import hash_password

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(name, email, password):
    if not name or not email or not password:
        return None, "All fields are required."
    if User.query.filter_by(email=email).first():
        return None, "Email already exists."
    hashed_pw = hash_password(password)
    user = User(name=name, email=email, password_hash=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return user, None

def update_user(user_id, name=None, email=None):
    user = User.query.get(user_id)
    if not user:
        return None
    if name:
        user.name = name
    if email:
        if User.query.filter_by(email=email).first():
            return None
        user.email = email
    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True
