from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'replace_with_strong_key'

    db.init_app(app)

    from app.routes.users import user_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def health():
        return {"status": "ok"}, 200

    return app
