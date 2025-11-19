from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Recado {self.titulo}>"
