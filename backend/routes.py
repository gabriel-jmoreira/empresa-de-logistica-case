from flask import Blueprint, request, jsonify, send_file
from flask_cors import cross_origin
from database import db
from models import Mercadoria
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

routes_bp = Blueprint('routes', __name__)  # Apenas um Blueprint

@routes_bp.route('/relatorio', methods=['GET'])
def gerar_relatorio():
    mercadorias = Mercadoria.query.all()
    caminho_pdf = "instance/relatorio.pdf"

    c = canvas.Canvas(caminho_pdf, pagesize=letter)
    c.drawString(100, 750, "Relatório de Mercadorias")

    y = 720
    for mercadoria in mercadorias:
        c.drawString(100, y, f"Nome: {mercadoria.nome} | Registro: {mercadoria.numero_registro} | "
                              f"Fabricante: {mercadoria.fabricante} | Tipo: {mercadoria.tipo} | "
                              f"Quantidade: {mercadoria.quantidade} | Data: {mercadoria.data.strftime('%Y-%m-%d')}")
        y -= 20

    c.save()
    return send_file(caminho_pdf, as_attachment=True)

@routes_bp.route('/mercadoria', methods=['GET', 'POST'])
@cross_origin()
def mercadorias():
    if request.method == 'POST':
        try:
            data = request.json
            nova_mercadoria = Mercadoria(
                nome=data['nome'],
                numero_registro=data['numero_registro'],  # Certifique-se de que existe no modelo
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
        'id': m.id, 'nome': m.nome, 'numero_registro': m.numero_registro,
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
