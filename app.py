from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CLIENTS_FILE = os.path.join(DATA_DIR, "clients.json")
FOURNISSEURS_FILE = os.path.join(DATA_DIR, "fournisseurs.json")
PRODUITS_FILE = os.path.join(DATA_DIR, "produits.json")
FACTURES_FILE = os.path.join(DATA_DIR, "factures.json")
DEVIS_FILE = os.path.join(DATA_DIR, "devis.json")

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/api/clients', methods=['GET'])
def get_clients():
    clients = load_data(CLIENTS_FILE)
    return jsonify(clients)

@app.route('/api/clients', methods=['POST'])
def add_client():
    data = request.json
    clients = load_data(CLIENTS_FILE)
    client = {
        'id': len(clients) + 1,
        'nom': data.get('nom'),
        'adresse': data.get('adresse'),
        'telephone': data.get('telephone'),
        'email': data.get('email')
    }
    clients.append(client)
    save_data(CLIENTS_FILE, clients)
    return jsonify(client), 201

@app.route('/api/fournisseurs', methods=['GET'])
def get_fournisseurs():
    fournisseurs = load_data(FOURNISSEURS_FILE)
    return jsonify(fournisseurs)

@app.route('/api/fournisseurs', methods=['POST'])
def add_fournisseur():
    data = request.json
    fournisseurs = load_data(FOURNISSEURS_FILE)
    fournisseur = {
        'id': len(fournisseurs) + 1,
        'nom': data.get('nom'),
        'adresse': data.get('adresse'),
        'telephone': data.get('telephone'),
        'email': data.get('email')
    }
    fournisseurs.append(fournisseur)
    save_data(FOURNISSEURS_FILE, fournisseurs)
    return jsonify(fournisseur), 201

@app.route('/api/produits', methods=['GET'])
def get_produits():
    produits = load_data(PRODUITS_FILE)
    return jsonify(produits)

@app.route('/api/produits', methods=['POST'])
def add_produit():
    data = request.json
    produits = load_data(PRODUITS_FILE)
    produit = {
        'id': len(produits) + 1,
        'nom': data.get('nom'),
        'reference': data.get('reference'),
        'prix_achat': data.get('prix_achat'),
        'prix_vente': data.get('prix_vente'),
        'fournisseur_id': data.get('fournisseur_id')
    }
    produits.append(produit)
    save_data(PRODUITS_FILE, produits)
    return jsonify(produit), 201

@app.route('/api/devis', methods=['GET'])
def get_devis():
    devis = load_data(DEVIS_FILE)
    return jsonify(devis)

@app.route('/api/devis', methods=['POST'])
def add_devis():
    data = request.json
    devis_list
