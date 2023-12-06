from .fornecedores import fornecedores_bp
from .conta_pagar import contas_pagar_bp
from .index import index_bp


def register_blueprints(app):
    app.register_blueprint(fornecedores_bp)
    app.register_blueprint(contas_pagar_bp)
    app.register_blueprint(index_bp)
