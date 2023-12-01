from flask import Flask
from models.database import db
from routes.routes import configure_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Adicione esta linha
db.init_app(app)

# Configurar rotas
configure_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
