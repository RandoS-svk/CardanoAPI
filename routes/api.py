from flask import Blueprint, jsonify, request
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

@api.route('/create-wallet', methods=["POST"])
def CreateWallet():
    if request.method == "POST":
        data = request.get_json()
        name = data['name']
        mnemonic_sentence = data['mnemonic_sentence']
        passphrase = data['passphrase']

        url = "http://localhost:8090/v2/wallets"
        payload = {
        "name": name,
        "mnemonic_sentence": mnemonic_sentence,
        "passphrase": passphrase,
        "address_pool_gap": 20
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers)
        response = response.json()
        return jsonify(response)


@api.route('/wallet/info/<string>')
def WalletInfo(string):
    url = f"http://localhost:8090/v2/wallets/{string}"
    response = requests.get(url)
    response = response.json()
    return jsonify(response)

api.route('/wallet/info/<string>/address')
def WalletAddress(string):
    url = f"http://localhost:8090/v2/wallets/{string}/addresses"
    response = requests.get(url)
    response = response.json()
    return jsonify(response)