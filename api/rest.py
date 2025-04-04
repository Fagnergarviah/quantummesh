from flask import Flask, jsonify, request
from blockchain.chain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transactions', methods=['POST'])
def new_transaction():
    data = request.get_json()
    blockchain.add_block(data)
    return jsonify({"status": "success"}), 201
