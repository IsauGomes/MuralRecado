from flask import Flask
from controllers.views import views
from models.modelo import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recados.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(views)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
