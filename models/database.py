from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"


class Fornecedores(db.Model):
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    nome_fornecedor = db.Column(db.String(100), nullable=False)
    contato_fornecedor = db.Column(db.String(50))
    endereco_fornecedor = db.Column(db.String(200))
    email_fornecedor = db.Column(db.String(50))


class ContasPagar(db.Model):
    id_conta = db.Column(db.Integer, primary_key=True)
    valor_conta = db.Column(db.Float, nullable=False)
    vencimento_conta = db.Column(db.Date, nullable=False)
    status_conta = db.Column(db.String(20), default='Pendente')
    tipo_conta = db.Column(db.String(20))

    # Chave estrangeira para Fornecedor
    fornecedor_id = db.Column(db.Integer, db.ForeignKey(
        'fornecedores.id_fornecedor'), nullable=False)
    fornecedor = db.relationship(
        'Fornecedores', backref=db.backref('contas_pagar', lazy=True))


class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    telefone_cliente = db.Column(db.String(20), nullable=True)
    tipo_cliente = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Cliente {self.nome_cliente}>"


class Vendas(db.Model):
    id_venda = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.Date, nullable=False)
    dinheiro_venda = db.Column(db.Float, nullable=True)
    deposito_venda = db.Column(db.Float, nullable=True)
    cartao_venda = db.Column(db.Float, nullable=True)
    cheques_venda = db.Column(db.Float, nullable=True)
    pix_venda = db.Column(db.Float, nullable=True)
    tipo_venda = db.Column(db.String(20), nullable=True)


class Cheques(db.Model):
    id_cheque = db.Column(db.Integer, primary_key=True)
    banco_cheque = db.Column(db.String(20), nullable=False, unique=False)
    conta_cheque = db.Column(db.String(20), nullable=False, unique=False)
    numero_cheque = db.Column(db.String(20), nullable=False, unique=False)
    valor_cheque = db.Column(db.Float, nullable=False)
    emitente_cheque = db.Column(db.String(100), nullable=False)
    recebimento_cheque = db.Column(db.Date, nullable=True)
    deposito_cheque = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default='Em Aberto')

    cliente_id = db.Column(db.Integer, db.ForeignKey(
        'clientes.id_cliente'), nullable=False)
    cliente = db.relationship(
        'Clientes', backref=db.backref('cheques', lazy=True))
    venda_id = db.Column(db.Integer, db.ForeignKey(
        'vendas.id_venda'), nullable=False)
    venda = db.relationship('Vendas', backref=db.backref('cheques', lazy=True))

    def __repr__(self):
        return f"""<Cheque {self.numero_cheque} -
            Valor: {self.valor_cheque} -
            Emitente: {self.emitente_cheque}>"""
