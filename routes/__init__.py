from .fornecedores import fornecedores_bp


def register_blueprints(app):
    app.register_blueprint(fornecedores_bp)
