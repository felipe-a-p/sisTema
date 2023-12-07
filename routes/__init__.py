from .fornecedores import fornecedores_bp
from .contas_pagar import contas_pagar_bp
from .clientes import clientes_bp
from .vendas import vendas_bp

from .index import index_bp


def register_blueprints(app):
    app.register_blueprint(fornecedores_bp)
    app.register_blueprint(contas_pagar_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(vendas_bp)
    app.register_blueprint(index_bp)
