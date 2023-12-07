from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, Vendas, Clientes
from forms import VendaForm

vendas_bp = Blueprint('vendas', __name__)

form = VendaForm


@vendas_bp.route('/vendas', methods=['GET', 'POST'])
def listar_vendas():
    # Consulta ao banco de dados para obter as vendas com informações do cliente
    vendas = db.session.query(Vendas, Clientes).join(
        Clientes, onclause=Vendas.cliente_id == Clientes.id_cliente).all()

    # Estrutura de dados para armazenar informações a serem exibidas na lista
    lista_vendas = []

    for venda, cliente in vendas:
        lista_vendas.append({
            'id_venda': venda.id_venda,
            'data_venda': venda.data_venda,
            'dinheiro_venda': venda.dinheiro_venda,
            'deposito_venda': venda.deposito_venda,
            'cartao_venda': venda.cartao_venda,
            'cheques_venda': venda.pix_venda,
            'tipo_venda': venda.tipo_venda,
            # Aqui obtemos o nome do cliente associado à venda
            'nome_cliente': cliente.nome_cliente
        })

    # Passe a lista para o template
    return render_template('vendas/vendas.html', vendas=lista_vendas)


@vendas_bp.route('/venda/nova', methods=['GET', 'POST'])
def nova_venda():
    form = VendaForm()
    form.cliente_id.choices = [
        (f.id_cliente, f.nome_cliente) for f in Clientes.query.all()]

    if form.validate_on_submit():
        nova_venda = Vendas(
            data_venda=form.data_venda.data,
            dinheiro_venda=form.dinheiro_venda.data,
            deposito_venda=form.deposito_venda.data,
            cartao_venda=form.cartao_venda.data,
            cheques_venda=form.cheques_venda.data,
            pix_venda=form.pix_venda.data,
            tipo_venda=form.tipo_venda.data,
            cliente_id=form.cliente_id.data
        )
        total_venda = (
            nova_venda.dinheiro_venda +
            nova_venda.deposito_venda +
            nova_venda.cartao_venda +
            nova_venda.cheques_venda +
            nova_venda.pix_venda
        )
        nova_venda.total_venda = total_venda
        db.session.add(nova_venda)
        db.session.commit()
        flash('Venda adicionada com sucesso!', 'success')
        return redirect(url_for('vendas.listar_vendas'))

    return render_template('vendas/venda.html', form=form,
                           modo='Nova')


@vendas_bp.route('/venda/<int:id>', methods=['GET', 'POST'])
def editar_conta(id):
    venda = Vendas.query.get_or_404(id)
    form = VendaForm(obj=venda)
    form.cliente_id.choices = [
        (f.cliente_id, f.nome_cliente) for f in Clientes.query.all()]

    if form.validate_on_submit():
        # Atualização do fornecedor com base nos dados do formulário
        venda.data_venda = form.data_venda.data
        venda.dinheiro_venda = form.dinheiro_venda.data
        venda.deposito_venda = form.deposito_venda.data
        venda.cartao_venda = form.cartao_venda.data
        venda.cheques_venda = form.cheques_venda.data
        venda.pix_venda = form.pix_venda.data
        venda.tipo_venda = form.tipo_venda.data
        total_venda = (
            venda.dinheiro_venda +
            venda.deposito_venda +
            venda.cartao_venda +
            venda.cheques_venda +
            venda.pix_venda
        )
        venda.total_venda = total_venda
        db.session.commit()
        return redirect(url_for('vendas.listar_vendas'))

    return render_template('vendas/venda.html',
                           form=form, venda=venda, modo="EDITAR")
