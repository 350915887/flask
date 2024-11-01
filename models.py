from datetime import datetime
from db import db


class User(db.Model):
    __tablename__ = 'db_user'

    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)  # 用户创建时间
    lastlogin = db.Column(db.DateTime, onupdate=datetime.utcnow)  # 最后一次登陆时间

    def __repr__(self):
        return f'<User {self.username}>'


class Data(db.Model):
    __tablename__ = 'db_data'

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, nullable=False)
    sensor_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    unit = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Data {self.id}>'


class Metric(db.Model):
    __tablename__ = 'db_metric'

    machine_id = db.Column(db.Integer, primary_key=True)
    precision = db.Column(db.Float, nullable=False)
    recall = db.Column(db.Float, nullable=False)
    f1 = db.Column(db.Float, nullable=False)
    TP = db.Column(db.Integer, nullable=False)
    FP = db.Column(db.Integer, nullable=False)
    TR = db.Column(db.Integer, nullable=False)
    FR = db.Column(db.Integer, nullable=False)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Metric machine_id={self.machine_id}>'


class Fault(db.Model):
    __tablename__ = 'db_fault'

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, nullable=False)
    solve = db.Column(db.Integer, nullable=False)
    fault_class = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<fault id={self.id}>'
