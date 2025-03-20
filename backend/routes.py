from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from database import db
from models import Mercadoria
from datetime import datetime

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/mercadoria', methods=['GET', 'POST'])
@cross_origin()  # ⬅️ Garante que CORS está habilitado para esta rota
def mercadorias():
    if request.method == 'POST':
        try:
            data = request.json
            nova_mercadoria = Mercadoria(
                nome=data['nome'],
                numero_registro=data['numero_registro'],
                fabricante=data['fabricante'],
                tipo=data['tipo'],
                quantidade=int(data['quantidade']),
                data=datetime.strptime(data['data'], '%Y-%m-%d')
            )
            db.session.add(nova_mercadoria)
            db.session.commit()
            return jsonify({'message': 'Mercadoria cadastrada!'}), 201
        except Exception as e:
            return jsonify({'error': f'Erro ao cadastrar mercadoria: {str(e)}'}), 400

    mercadorias = Mercadoria.query.all()
    return jsonify([{
        'id': m.id, 'nome': m.nome, 'registro': m.numero_registro,
        'fabricante': m.fabricante, 'tipo': m.tipo, 'quantidade': m.quantidade,
        'data': m.data.strftime('%Y-%m-%d')
    } for m in mercadorias])

@routes_bp.route('/mercadoria/<int:id>', methods=['PUT'])
@cross_origin()
def editar_mercadoria(id):
    data = request.json
    mercadoria = Mercadoria.query.get(id)
    
    if not mercadoria:
        return jsonify({'message': 'Mercadoria não encontrada'}), 404

    mercadoria.nome = data.get('nome', mercadoria.nome)
    mercadoria.numero_registro = data.get('numero_registro', mercadoria.numero_registro)
    mercadoria.fabricante = data.get('fabricante', mercadoria.fabricante)
    mercadoria.tipo = data.get('tipo', mercadoria.tipo)
    mercadoria.descricao = data.get('descricao', mercadoria.descricao)
    mercadoria.quantidade = data.get('quantidade', mercadoria.quantidade)
    
    db.session.commit()
    return jsonify({'message': 'Mercadoria atualizada com sucesso'})

@routes_bp.route('/mercadoria/<int:id>', methods=['DELETE'])
@cross_origin()
def excluir_mercadoria(id):
    mercadoria = Mercadoria.query.get(id)
    
    if not mercadoria:
        return jsonify({'message': 'Mercadoria não encontrada'}), 404
    
    db.session.delete(mercadoria)
    db.session.commit()
    return jsonify({'message': 'Mercadoria excluída com sucesso'})
