from flask import Flask, request, jsonify
from flask_cors import CORS
from drawbot import get_drawish_move_from_fen

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello from Flask backend!!'

@app.route('/drawbot-move', methods=['POST'])
def drawbot_move():
    data = request.get_json()
    fen = data.get('fen')
    move = get_drawish_move_from_fen(fen)
    print("Received FEN:", fen)
    print(move)
    return jsonify({'move': move})