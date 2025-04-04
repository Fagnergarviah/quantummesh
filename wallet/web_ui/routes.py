from flask import render_template, request, jsonify, redirect, url_for
from wallet.web_ui.app import app
from wallet.keys import Wallet
from blockchain.transaction import Transaction

@app.route('/send', methods=['GET', 'POST'])
def send_transaction():
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        amount = float(request.form.get('amount'))
        
        wallet = Wallet()
        tx = Transaction(
            sender=wallet.get_address(),
            receiver=recipient,
            amount=amount
        )
        tx.sign(wallet.private_key)
        
        # Aqui você adicionaria o código para enviar a transação para a rede
        return redirect(url_for('index'))
    
    return render_template('send.html')

@app.route('/api/balance/<address>')
def api_balance(address):
    # Implementação real buscaria do blockchain
    return jsonify({'balance': 1000, 'address': address})
