# webhook_server.py
# Este é um exemplo simples de um servidor Flask que recebe webhooks do GitHub.

from flask import Flask, request, jsonify

app = Flask(__name__)  # inicializa a aplicação Flask

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Recebido webhook do GitHub:")
    print(data)

    if 'workflow_run' in data:
        status = data['workflow_run']['status']
        conclusion = data['workflow_run'].get('conclusion', 'N/A')
        name = data['workflow_run']['name']
        run_number = data['workflow_run']['run_number']

        status_msg = f"Workflow: {name} | Run #{run_number} | Status: {status} | Resultado: {conclusion}"
        print(status_msg)

        with open("status.txt", "w", encoding='utf-8') as f:
            f.write(status_msg)

    return jsonify({'message': 'Webhook processado com sucesso!'}), 200

# Executa o servidor localmente na porta 5000
if __name__ == '__main__':
    app.run(port=5000)
