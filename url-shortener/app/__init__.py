from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.shortener import shortener_bp
    app.register_blueprint(shortener_bp)

    @app.route("/")
    def health():
        return {"status": "ok"}, 200

    return app
