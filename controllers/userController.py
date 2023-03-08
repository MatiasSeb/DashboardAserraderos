import bcrypt
from models.userModels import User, Role
from config.database import session_users

def create_user(username, email, password, role_id):
    hashed_password = hash_password(password)
    user = User(username=username, email=email, password=hashed_password, role_id=role_id)
    session_users.add(user)
    session_users.commit()

def get_user_by_name(username):
    user = User.query.filter_by(username=username).first()
    return user

def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

def get_all_users():
    users = User.query.all()
    return users

def delete_user(username):
    user = User.query.filter_by(username=username).first()
    session_users.delete(user)
    session_users.commit()

def update_user(email, new_email, new_role_id):
    user = get_user_by_email(email)
    user.email = new_email
    user.role_id = new_role_id
    session_users.commit()

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_role_by_id(role_id):
    role = Role.query.filter_by(id=role_id).first()
    return role

def get_role_by_name(role_name):
    role = Role.query.filter_by(name=role_name).first()
    return role
