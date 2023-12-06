from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, ContasPagar, Fornecedores
from forms import ContaPagarForm

contas_pagar_bp = Blueprint('contas_pagar', __name__)

form = ContaPagarForm


@contas_pagar_bp.route('/contas_pagar', methods=['GET', 'POST'])
def listar_contas_pagar():
    # Consulta ao banco de dados para obter as contas a pagar com os nomes dos fornecedores
    contas = db.session.query(
        ContasPagar, Fornecedores).join(Fornecedores).all()

    # Estrutura de dados para armazenar informações a serem exibidas na lista
    lista_contas = []

    for conta, fornecedor in contas:
        lista_contas.append({
            'id_conta': conta.id_conta,
            'valor_conta': conta.valor_conta,
            'vencimento_conta': conta.vencimento_conta,
            'status_conta': conta.status_conta,
            'tipo_conta': conta.tipo_conta,
            # Aqui obtemos o nome do fornecedor
            'nome_fornecedor': fornecedor.nome_fornecedor
        })

    # Passe a lista para o template
    return render_template('contas_pagar/contas_pagar.html',
                           contas_pagar=lista_contas,
                           form=form)


@contas_pagar_bp.route('/conta_pagar/nova', methods=['GET', 'POST'])
def nova_conta_pagar():
    form = ContaPagarForm()
    form.fornecedor_id.choices = [
        (f.id_fornecedor, f.nome_fornecedor) for f in Fornecedores.query.all()]

    if form.validate_on_submit():
        nova_conta = ContasPagar(
            valor_conta=form.valor_conta.data,
            vencimento_conta=form.vencimento_conta.data,
            status_conta=form.status_conta.data,
            tipo_conta=form.tipo_conta.data,
            fornecedor_id=form.fornecedor_id.data
        )
        db.session.add(nova_conta)
        db.session.commit()
        flash('Conta adicionada com sucesso!', 'success')
        return redirect(url_for('contas_pagar.listar_contas_pagar'))

    return render_template('contas_pagar/conta_pagar.html', form=form,
                           modo='Nova')
