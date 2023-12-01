from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"


class Fornecedor(db.Model):
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    nome_fornecedor = db.Column(db.String(100), nullable=False)
    contato_fornecedor = db.Column(db.String(50))
    endereco_fornecedor = db.Column(db.String(200))


class ContaPagar(db.Model):
    id_conta = db.Column(db.Integer, primary_key=True)
    valor_conta = db.Column(db.Float, nullable=False)
    vencimento_conta = db.Column(db.Date, nullable=False)
    status_conta = db.Column(db.String(20), default='Pendente')
    tipo_conta = db.Column(db.String(20))

    # Chave estrangeira para Fornecedor
    fornecedor_id = db.Column(db.Integer, db.ForeignKey(
        'fornecedor.id_fornecedor'), nullable=False)
    fornecedor = db.relationship(
        'Fornecedor', backref=db.backref('contas_pagar', lazy=True))


class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Cliente {self.nome} - Email: {self.email}>"


class Cheque(db.Model):
    id_cheque = db.Column(db.Integer, primary_key=True)
    banco_cheque = db.Column(db.String(20), nullable=False, unique=False)
    conta_cheque = db.Column(db.String(20), nullable=False, unique=False)
    numero_cheque = db.Column(db.String(20), nullable=False, unique=False)
    valor_cheque = db.Column(db.Float, nullable=False)
    emitente_cheque = db.Column(db.String(100), nullable=False)
    recebimento_cheque = db.Column(db.Date, nullable=True)
    deposito_cheque = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default='Em Aberto')
    # Fks
    cliente_id = db.Column(db.Integer, db.ForeignKey(
        'cliente.id_cliente'), nullable=False)
    cliente = db.relationship(
        'Cliente', backref=db.backref('cheques', lazy=True))

    def __repr__(self):
        return (f"""<Cheque {self.numero_cheque} -
                Valor: {self.numero_cheque} -
                Emitente: {self.emitente_cheque}>""")
