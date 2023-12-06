from flask import render_template, redirect, url_for, request
import forms
from models.database import db, Cheques, Vendas, Fornecedores, Clientes, ContasPagar


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cheques/novo', methods=['GET', 'POST'])
    def novo_cheque():
        form = forms.ChequeForm()

        if form.validate_on_submit():
            novo_cheque = Cheques(
                banco_cheque=form.banco_cheque.data,
                conta_cheque=form.conta_cheque.data,
                numero_cheque=form.numero_cheque.data,
                valor_cheque=form.valor_cheque.data,
                emitente_cheque=form.emitente_cheque.data,
                recebimento_cheque=form.recebimento_cheque.data,
                deposito_cheque=form.deposito_cheque.data,
                status=form.status.data
            )

            db.session.add(novo_cheque)
            db.session.commit()

            return redirect(url_for('listar_cheques'))

        return render_template('novo_cheque.html', form=form)

    @app.route('/cheques')
    def lista_cheques():
        # Obtenha os critérios de busca do formulário
        filtro_emitente = request.args.get('filtro_emitente', '')

        # Consulte o banco de dados aplicando os filtros
        # (substitua esta lógica pela lógica real de consulta ao banco de dados)
        cheques = consultar_banco_de_dados(filtro_emitente)

        return render_template('listar_cheques.html', cheques=cheques)

    @app.route('/vendas/nova', methods=['GET', 'POST'])
    def nova_venda():
        form = forms.VendaForm()

        if form.validate_on_submit():
            nova_venda = Vendas(
                data_venda=form.data_venda.data,
                dinheiro_venda=form.dinheiro_venda.data,
                deposito_venda=form.deposito_venda.data,
                cartao_venda=form.cartao_venda.data,
                cheques_venda=form.cheques_venda.data,
                pix_venda=form.pix_venda.data,
                tipo_venda=form.tipo_venda.data
            )

            db.session.add(nova_venda)
            db.session.commit()

            return redirect(url_for('listar_vendas'))

        return render_template('nova_venda.html', form=form)

    @app.route('/vendas')
    def listar_vendas():
        vendas = Vendas.query.all()
        return render_template('listar_vendas.html', vendas=vendas)

    @app.route('/fornecedores/novo', methods=['GET', 'POST'])
    def novo_fornecedor():
        form = forms.FornecedorForm()

        if form.validate_on_submit():
            novo_fornecedor = Fornecedores(
                nome_fornecedor=form.nome_fornecedor.data,
                contato_fornecedor=form.contato_fornecedor.data,
                endereco_fornecedor=form.endereco_fornecedor.data,
                email_fornecedor=form.email_fornecedor.data
            )

            db.session.add(novo_fornecedor)
            db.session.commit()

            return redirect(url_for('listar_fornecedores'))

        return render_template('novo_fornecedor.html', form=form)

    @app.route('/fornecedores')
    def listar_fornecedores():
        fornecedores = Fornecedores.query.all()
        return render_template('listar_fornecedores.html',
                               fornecedores=fornecedores)

    @app.route('/clientes/novo', methods=['GET', 'POST'])
    def novo_cliente():
        form = forms.ClienteForm()

        if form.validate_on_submit():
            novo_cliente = Clientes(
                nome_cliente=form.nome_cliente.data,
                telefone_cliente=form.telefone_cliente.data,
                tipo_cliente=form.tipo_cliente.data
            )

            db.session.add(novo_cliente)
            db.session.commit()

            return redirect(url_for('listar_clientes'))

        return render_template('novo_cliente.html', form=form)

    @app.route('/clientes')
    def listar_clientes():
        clientes = Clientes.query.all()
        return render_template('listar_clientes.html', clientes=clientes)

    @app.route('/contas_pagar/nova', methods=['GET', 'POST'])
    def nova_conta_pagar():
        form = forms.ContaPagarForm()

        # Preencher o campo de seleção de fornecedores
        form.fornecedor_id.choices = [
            (f.id_fornecedor, f.nome_fornecedor) for f in Fornecedores.query.all()]

        if form.validate_on_submit():
            nova_conta_pagar = ContasPagar(
                valor_conta=form.valor_conta.data,
                vencimento_conta=form.vencimento_conta.data,
                status_conta=form.status_conta.data,
                tipo_conta=form.tipo_conta.data,
                fornecedor_id=form.fornecedor_id.data
            )

            db.session.add(nova_conta_pagar)
            db.session.commit()

            return redirect(url_for('listar_contas_pagar'))

        return render_template('nova_conta_pagar.html', form=form)

    @app.route('/contas_pagar')
    def listar_contas_pagar():
        contas_pagar = ContasPagar.query.all()
        return render_template('listar_contas_pagar.html',
                               contas_pagar=contas_pagar)
