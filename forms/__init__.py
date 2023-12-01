from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class ChequeForm(FlaskForm):
    banco_cheque = StringField('Banco', validators=[DataRequired()])
    conta_cheque = StringField('Conta', validators=[DataRequired()])
    numero_cheque = StringField('Número', validators=[DataRequired()])
    valor_cheque = FloatField(
        'Valor', validators=[DataRequired(), NumberRange(min=0)])
    emitente_cheque = StringField('Emitente', validators=[DataRequired()])
    recebimento_cheque = DateField('Recebimento', format='%Y-%m-%d')
    deposito_cheque = DateField('Depósito', format='%Y-%m-%d')
    status = SelectField('Status', choices=[
                        ('Em Aberto', 'Em Aberto'), ('Pago', 'Pago')],
        default='Em Aberto')
    submit = SubmitField('Salvar')


class FornecedorForm(FlaskForm):
    nome_fornecedor = StringField(
        'Nome do Fornecedor', validators=[DataRequired()])
    contato_fornecedor = StringField('Contato do Fornecedor')
    endereco_fornecedor = TextAreaField('Endereço do Fornecedor')
    email_fornecedor = StringField('Email do Fornecedor')
    submit = SubmitField('Salvar')


class VendaForm(FlaskForm):
    data_venda = DateField(
        'Data da Venda', format='%Y-%m-%d', validators=[DataRequired()])
    dinheiro_venda = FloatField('Dinheiro', validators=[NumberRange(min=0)])
    deposito_venda = FloatField('Depósito', validators=[NumberRange(min=0)])
    cartao_venda = FloatField('Cartão', validators=[NumberRange(min=0)])
    cheques_venda = FloatField('Cheques', validators=[NumberRange(min=0)])
    pix_venda = FloatField('PIX', validators=[NumberRange(min=0)])
    tipo_venda = SelectField('Tipo de Venda', choices=[(
        'Mercadoria', 'Mercadoria'), ('Serviço', 'Serviço')],
        validators=[DataRequired()])
    submit = SubmitField('Salvar')


class ClienteForm(FlaskForm):
    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    telefone_cliente = StringField('Telefone do Cliente')
    tipo_cliente = SelectField('Tipo de Cliente', choices=[(
        'Regular', 'Regular'), ('VIP', 'VIP')], validators=[DataRequired()])
    submit = SubmitField('Salvar')


class ContaPagarForm(FlaskForm):
    valor_conta = FloatField('Valor da Conta', validators=[DataRequired()])
    vencimento_conta = DateField(
        'Vencimento da Conta', format='%Y-%m-%d', validators=[DataRequired()])
    status_conta = SelectField('Status da Conta', choices=[(
        'Pendente', 'Pendente'), ('Pago', 'Pago')], validators=[DataRequired()])
    tipo_conta = SelectField('Tipo de Conta', choices=[(
        'Despesa', 'Despesa'), ('Fatura', 'Fatura')], validators=[DataRequired()])
    fornecedor_id = SelectField(
        'Fornecedor', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar')
