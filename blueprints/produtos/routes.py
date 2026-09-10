from flask import render_template, request, session
from . import produtos_bp
import models

@produtos_bp.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        lista = models.buscar_por_nome(q)
    else:
        lista = models.produtos
    return render_template("produtos/index.html", produtos=lista, q=q, user=session.get('usuario', None),
                           categorias=models.todas_categorias())

@produtos_bp.route("/produto/<int:produto_id>")
def ver_produto(produto_id):
    produto = models.buscar_produto(produto_id)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template("produtos/detalhes.html", produto=produto,user=session.get('usuario', None))

@produtos_bp.route("/categoria/<nome>")
def ver_categoria(nome):
    lista = models.buscar_por_categoria(nome)
    return render_template("produtos/index.html", produtos=lista, q="", user=session.get('usuario', None),
                           categorias=models.todas_categorias())