from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # 注册蓝图模块
    from app.routes.auth import bp as auth_bp
    from app.routes.main import bp as main_bp
    from app.routes.yolo import bp as yolo_bp
    from app.routes.speech import bp as speech_bp
    from app.routes.nlp import bp as nlp_bp
    from app.routes.ocr import bp as ocr_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(yolo_bp)
    app.register_blueprint(speech_bp)
    app.register_blueprint(nlp_bp)
    app.register_blueprint(ocr_bp)

    # 登录用户加载器（延迟导入）
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
