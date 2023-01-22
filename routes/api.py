from flask import Blueprint, jsonify
import requests

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/node-info')
def NodeInfo():
    url = "http://localhost:8090/v2/network/information"
    response = requests.get(url)
    response = response.json()
    response = response['sync_progress']
    status = response['status']
    
    if status == 'ready':
        return jsonify({
            'status': 'ready',
            'blockchain': 'cardano_blockchain'
        })
    else:
        quantity = response['progress']
        quantity = quantity['quantity']
        return jsonify({
            'status': status,
            'quantity': quantity,
            'blockchain': 'cardano_blockchain'
        })