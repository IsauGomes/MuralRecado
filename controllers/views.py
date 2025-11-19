from flask import Blueprint, render_template, request, redirect, url_for
from models.modelo import db, Recado

views = Blueprint("views", __name__)

@views.route("/")
def index():
    busca = request.args.get("busca", "")
    if busca:
        recados = Recado.query.filter(
            Recado.titulo.ilike(f"%{busca}%") |
            Recado.autor.ilike(f"%{busca}%")
        ).all()
    else:
        recados = Recado.query.all()

    return render_template("index.html", recados=recados, busca=busca)



@views.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        mensagem = request.form.get("mensagem")

        novo = Recado(titulo=titulo, autor=autor, mensagem=mensagem)
        db.session.add(novo)
        db.session.commit()

        return redirect(url_for("views.index"))

    return render_template("criar.html")


@views.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    recado = Recado.query.get(id)

    if request.method == "POST":
        recado.titulo = request.form.get("titulo")
        recado.autor = request.form.get("autor")
        recado.mensagem = request.form.get("mensagem")

        db.session.commit()
        return redirect(url_for("views.index"))

    return render_template("editar.html", recado=recado)


@views.route("/deletar/<int:id>")
def deletar(id):
    recado = Recado.query.get(id)
    db.session.delete(recado)
    db.session.commit()
    return redirect(url_for("views.index"))
