from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///examplee.db'  # Pode ser MySQL, PostgreSQL etc.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Campo obrigatório
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)  # Valor padrão
    is_active = db.Column(db.Boolean, default=True)  # Valor booleano

user = User(name="John", email="john@example.com")
db.session.add(user)  # Adiciona o usuário à sessão
db.session.commit()   # Confirma a inserção no banco de dados

try:
    db.session.commit()  # Tenta confirmar as alterações
except Exception as e:
    db.session.rollback()  # Se falhar, desfaz as alterações na sessão
    print(f"Erro: {e}")
