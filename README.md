Empresa Logística

Descrição

Este é um sistema de gestão de mercadorias para uma empresa logística. Ele permite o cadastro, listagem e geração de relatórios de mercadorias.

Tecnologias Utilizadas

Backend: Flask, Flask-SQLAlchemy, Flask-CORS, ReportLab (para PDF)

Banco de Dados: SQLite

Frontend: React, Axios, React Modal

Funcionalidades

Cadastro de mercadorias com nome, número de registro, fabricante, tipo, quantidade e data de entrada

Listagem das mercadorias cadastradas

Geração de relatórios diários em PDF

Edição e exclusão de mercadorias

Requisitos

Python 3.10+

Node.js 16+

Como Rodar o Projeto

Backend

Clone o repositório:

Crie um ambiente virtual e instale as dependências:

Execute o backend:

Frontend

Acesse a pasta frontend:

Instale as dependências:

Inicie o frontend:

API Endpoints

Mercadorias

GET /mercadoria - Lista todas as mercadorias

POST /mercadoria - Cadastra uma nova mercadoria

PUT /mercadoria/<id> - Edita uma mercadoria

DELETE /mercadoria/<id> - Remove uma mercadoria

Relatório

GET /relatorio - Gera e baixa um relatório em PDF
