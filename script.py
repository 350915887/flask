from models import User
from db import db, init_app
from werkzeug.security import generate_password_hash

app = init_app()


def add_user(username, password, role, email):
    new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2'), role=role, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} added successfully."


def delete_users(username):
    # 查找所有具有特定用户名的用户
    result = User.query.filter_by(username=username).delete()
    # 提交更改
    db.session.commit()
    return f"Deleted {result} users with username '{username}'."


if __name__ == '__main__':
    with app.app_context():
        delete_users('黎子梁')
        add_user('黎子梁', '123456', 'admin', '350915887@qq.com')
