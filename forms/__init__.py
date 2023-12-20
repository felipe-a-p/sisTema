# forms
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Length


class FornecedorForm(FlaskForm):
    nome_fornecedor = StringField(
        'Nome do Fornecedor', validators=[DataRequired()])
    contato_fornecedor = StringField('Contato do Fornecedor')
    endereco_fornecedor = TextAreaField('Endereço do Fornecedor')
    email_fornecedor = StringField('Email do Fornecedor')
    submit = SubmitField('Salvar')


class ClienteForm(FlaskForm):
    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    telefone_cliente = StringField('Telefone do Cliente')
    tipo_cliente = SelectField('Tipo de Cliente', choices=[(
        'Regular', 'Regular'), ('VIP', 'VIP')], validators=[DataRequired()])
    submit = SubmitField('Salvar')


class VendaForm(FlaskForm):
    data_venda = DateField('Data da Venda', validators=[DataRequired()])
    dinheiro_venda = FloatField('Dinheiro')
    deposito_venda = FloatField('Depósito Bancário')
    cartao_venda = FloatField('Cartão de Crédito')
    cheques_venda = FloatField('Cheques')
    pix_venda = FloatField('Pix')
    tipo_venda = SelectField('Tipo de Venda', choices=[('Produto', 'Produto'), ('Serviço', 'Serviço')],
                             validators=[DataRequired()])
    cliente_id = SelectField('Cliente', coerce=int,
                             validators=[DataRequired()])
    total_venda = FloatField('Total Venda')
    submit = SubmitField('Salvar')


class ContaPagarForm(FlaskForm):
    valor_conta = FloatField('Valor da Conta', validators=[DataRequired()])
    vencimento_conta = DateField(
        'Vencimento da Conta', format='%Y-%m-%d', validators=[DataRequired()])
    status_conta = SelectField('Status da Conta', choices=[(
        'Pendente', 'Pendente'),
        ('Pago', 'Pago')], validators=[DataRequired()])
    tipo_conta = SelectField('Tipo de Conta',
                             choices=[('Produto Acabado', 'Produto Acabado'),
                                      ('Materia Prima',
                                       'Materia Prima'),
                                      ('Servico', 'Servico'),
                                      ('Imposto', 'Imposto'),
                                      ('Colaboradores', 'Colaboradores'),
                                      ('Outros', 'Outros')],
                             validators=[DataRequired()])
    fornecedor_id = SelectField(
        'Fornecedor', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Salvar')


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')


class ChequeForm(FlaskForm):
    banco_cheque = StringField('Banco do Cheque', validators=[
                               InputRequired(), Length(max=20)])
    conta_cheque = StringField('Conta do Cheque', validators=[
                               InputRequired(), Length(max=20)])
    numero_cheque = StringField('Número do Cheque', validators=[
                                InputRequired(), Length(max=20)])
    valor_cheque = FloatField('Valor do Cheque', validators=[InputRequired()])
    emitente_cheque = StringField('Emitente do Cheque', validators=[
                                  InputRequired(), Length(max=100)])
    recebimento_cheque = DateField(
        'Data de Recebimento', format='%Y-%m-%d', validators=[])
    deposito_cheque = DateField(
        'Data de Depósito', format='%Y-%m-%d', validators=[])
    status = SelectField('Status do Cheque', choices=[
        ('Em Aberto', 'Em Aberto'),
        ('Depositado', 'Depositado'),
        ('Devolvido', 'Devolvido')],
        default='Em Aberto', validators=[InputRequired()])
    cliente_id = SelectField('ID do Cliente', coerce=int,
                             validators=[InputRequired()])
    venda_id = SelectField('ID da Venda', coerce=int,
                           validators=[InputRequired()])
