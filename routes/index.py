# fornecedores.py
from flask import Blueprint, render_template, redirect, url_for
from models import db, Fornecedores
from forms import FornecedorForm

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index.html')
