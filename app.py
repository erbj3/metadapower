from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/player', methods=['GET'])
def get_player_data():
    try:
        player_url = request.args.get('url')
        if not player_url:
            return jsonify({"error": "A URL do player não foi fornecida."}), 400

        response = requests.get(player_url)
        if response.status_code != 200:
            return jsonify({"error": "Erro ao acessar o player."}), 500

        data = response.json()
        return jsonify({
            "artist": data.get("artist", "Desconhecido"),
            "title": data.get("title", "Desconhecido"),
            "status": data.get("status", "Desconhecido"),
            "listeners": data.get("listeners", 0),
            "image": data.get("image")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
