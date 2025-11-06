from flask import Flask
from backend.config import DB_PATH
from backend.models.user_model import db as db_user
from backend.models.event_model import db as db_event
from backend.models.notification_log_model import db as db_log
from backend.routes.auth_routes import auth_bp
from backend.routes.user_routes import user_bp
from backend.routes.event_routes import event_bp
from backend.routes.notification_routes import notification_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "supersecretkey"

    db_user.init_app(app)
    db_event.init_app(app)
    db_log.init_app(app)
    with app.app_context():
        db_user.create_all()
        db_event.create_all()
        db_log.create_all()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(event_bp, url_prefix="/api")
    app.register_blueprint(notification_bp, url_prefix="/api")

    return app
