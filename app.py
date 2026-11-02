"""Ponto de entrada do monólito modular da Livraria."""
from flask import Flask, render_template
from modules.catalog import catalog_bp
from modules.users import users_bp
from modules.reservations import reservations_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(reservations_bp)

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
