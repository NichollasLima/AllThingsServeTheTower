# webhook.server.py
# Este é um exemplo simples de um servidor Flask que recebe webhooks do GitHub.
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Recebido webhook do GitHub:")
    print(data)  # Aqui você pode tratar o evento e salvar/usar info como quiser

    # Responde para o GitHub que recebeu o webhook
    return jsonify({'message': 'Webhook recebido com sucesso!'}), 200

if __name__ == '__main__':
    app.run(port=5000)