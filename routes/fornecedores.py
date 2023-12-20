# fornecedores.py
from flask import Blueprint, render_template, redirect, url_for
from models import db, Fornecedores
from forms import FornecedorForm

fornecedores_bp = Blueprint('fornecedores', __name__)

form = FornecedorForm


@fornecedores_bp.route('/fornecedores', methods=['GET', 'POST'])
def listar_fornecedores():
    form = FornecedorForm()

    # Lógica para obter a lista de fornecedores do banco de dados
    fornecedores = Fornecedores.query.all()

    return render_template('fornecedores/fornecedores.html',
                           fornecedores=fornecedores,
                           form=form)


@fornecedores_bp.route('/fornecedor/novo', methods=['GET', 'POST'])
def novo_fornecedor():
    form = FornecedorForm()  # Crie uma instância do formulário aqui

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
        return redirect(url_for('fornecedores.listar_fornecedores', mensagem='Fornecedor criado com sucesso!'))

    return render_template('fornecedores/fornecedor.html', form=form, modo="ADICIONAR")


@fornecedores_bp.route('/fornecedor/<int:id>', methods=['GET', 'POST'])
def editar_fornecedor(id):
    fornecedor = Fornecedores.query.get_or_404(id)
    form = FornecedorForm(obj=fornecedor)

    if form.validate_on_submit():
        # Atualização do fornecedor com base nos dados do formulário
        fornecedor.nome_fornecedor = form.nome_fornecedor.data
        fornecedor.contato_fornecedor = form.contato_fornecedor.data
        fornecedor.endereco_fornecedor = form.endereco_fornecedor.data
        fornecedor.email_fornecedor = form.email_fornecedor.data

        db.session.commit()
        return redirect(url_for('fornecedores.listar_fornecedores', mensagem='Fornecedor editado com sucesso!'))

    return render_template('fornecedores/fornecedor.html',
                           form=form, fornecedor=fornecedor, modo="EDITAR")
