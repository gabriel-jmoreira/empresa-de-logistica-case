from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database import db
from routes import routes_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistica.db'
db.init_app(app)

# 🔥 Registra o Blueprint para manter as rotas organizadas
app.register_blueprint(routes_bp)

# Criar o banco de dados (se ainda não existir)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
