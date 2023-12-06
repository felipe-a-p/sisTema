# fornecedores.py
from flask import Blueprint, render_template, redirect, url_for
from models import db, Fornecedores
from forms import FornecedorForm

fornecedores_bp = Blueprint('fornecedores', __name__)


@fornecedores_bp.route('/fornecedores', methods=['GET', 'POST'])
def listar_fornecedores():
    form = FornecedorForm()

    if form.validate_on_submit():
        # Criação de um novo fornecedor
        novo_fornecedor = Fornecedores(
            nome_fornecedor=form.nome_fornecedor.data,
            contato_fornecedor=form.contato_fornecedor.data,
            endereco_fornecedor=form.endereco_fornecedor.data,
            email_fornecedor=form.email_fornecedor.data
        )
        db.session.add(novo_fornecedor)
        db.session.commit()
        return redirect(url_for('fornecedores.listar_fornecedores'))

    # Lógica para obter a lista de fornecedores do banco de dados
    fornecedores = Fornecedores.query.all()

    return render_template('fornecedores/fornecedores.html',
                           fornecedores=fornecedores,
                           form=form)
