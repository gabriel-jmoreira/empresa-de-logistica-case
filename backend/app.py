from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database import db
from routes import routes_bp

app = Flask(__name__)

# 🔥 CONFIGURAR CORS PARA ACEITAR REQUISIÇÕES DO FRONTEND
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistica.db'
db.init_app(app)

app.register_blueprint(routes_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
