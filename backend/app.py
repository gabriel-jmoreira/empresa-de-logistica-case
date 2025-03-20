from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
from routes import routes_bp

app = Flask(__name__)

# Configuração do banco de dados (SQLite por padrão)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Criar tabelas antes de rodar o servidor
with app.app_context():
    db.create_all()

# Registrar Blueprint das rotas
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)
