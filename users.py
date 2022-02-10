from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

# TODO: käyttäjätietojen syöttö ja päivitys

def user_id():
    return session.get("user_id",0)

def is_admin(user_id):
    sql = "SELECT COUNT(*) FROM users_roles WHERE user_id=:user_id AND role_id=:role_id"
    result = db.session.execute(sql, {"user_id":user_id, "role_id":1})
    row = result.fetchone()
    if row.count > 0:
        return True
    else:
        return False

def is_tutor(user_id):
    sql = "SELECT COUNT(*) FROM users_roles WHERE user_id=:user_id AND role_id=:role_id"
    result = db.session.execute(sql, {"user_id":user_id, "role_id":2})
    row = result.fetchone()
    if row.count > 0:
        return True
    else:
        return False

def is_fresher(user_id):
    sql = "SELECT COUNT(*) FROM users_roles WHERE user_id=:user_id AND role_id=:role_id"
    result = db.session.execute(sql, {"user_id":user_id, "role_id":3})
    row = result.fetchone()
    if row.count > 0:
        return True
    else:
        return False