from flask import render_template, redirect, url_for, request
import forms
from models.database import db, Cheques, Vendas, Fornecedores, Clientes, ContasPagar


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
