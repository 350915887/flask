from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# 创建一个SQLAlchemy对象，它将用于我们的数据库操作
db = SQLAlchemy()


def init_app():
    # 创建一个 Flask 应用实例
    app = Flask(__name__)
    # 配置数据库的 URI，这里使用 SQLite 数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fault_diagnosis.db'
    # 禁用 Flask-SQLAlchemy 事件系统，不跟踪对象的修改状态
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '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'

    # 将上面创建的 app 绑定到 SQLAlchemy db 对象
    db.init_app(app)

    # 在应用上下文中创建所有定义的数据库表
    with app.app_context():
        db.create_all()

    # 返回配置好的 Flask 应用
    return app
