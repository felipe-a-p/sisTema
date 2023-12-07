# app.py
from flask import Flask
from models import db
from routes import register_blueprints
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


app = Flask(__name__, template_folder='templates')
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

csrf = CSRFProtect(app)


# Configurações do Banco de Dados (você deve ter algo assim no seu projeto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:/felip/Documents/Git/sisTema/sisTema/instance/site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Pc-Server/Documents/GitHub/sisTema/instance/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialize o banco de dados
db.init_app(app)
with app.app_context():
    db.create_all()

# Registre todos os blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
