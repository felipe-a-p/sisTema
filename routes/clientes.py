from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, Clientes
from forms import ClienteForm

clientes_bp = Blueprint('clientes', __name__)

form = ClienteForm


@clientes_bp.route('/clientes', methods=['GET', 'POST'])
def listar_clientes():
    form = ClienteForm()
    clientes = db.session.query(
        Clientes)

    # Estrutura de dados para armazenar informações a serem exibidas na lista
    lista_clientes = []

    for cliente in clientes:
        lista_clientes.append({
            'id_cliente': cliente.id_cliente,
            'nome_cliente': cliente.nome_cliente,
            'telefone_cliente': cliente.telefone_cliente,
            'tipo_cliente': cliente.tipo_cliente,
        })

    # Passe a lista para o template
    return render_template('clientes/clientes.html',
                           clientes=lista_clientes,
                           form=form)


@clientes_bp.route('/cliente/novo', methods=['GET', 'POST'])
def novo_cliente():
    form = ClienteForm()

    if form.validate_on_submit():
        novo_cliente = Clientes(
            nome_cliente=form.nome_cliente.data,
            telefone_cliente=form.telefone_cliente.data,
            tipo_cliente=form.tipo_cliente.data,

        )
        db.session.add(novo_cliente)
        db.session.commit()
        flash('Cliente adicionado com sucesso!', 'success')
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('clientes/cliente.html', form=form,
                           modo='Nova')


@clientes_bp.route('/cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Clientes.query.get_or_404(id)
    form = ClienteForm(obj=cliente)

    if form.validate_on_submit():
        # Atualização do cliente com base nos dados do formulário
        cliente.nome_cliente = form.nome_cliente.data
        cliente.telefone_cliente = form.telefone_cliente.data
        cliente.tipo_cliente = form.tipo_cliente.data

        db.session.commit()
        flash('Cliente atualizado com sucesso!', 'success')
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('clientes/cliente.html', form=form, cliente=cliente, modo="EDITAR")
