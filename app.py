from flask import Flask, jsonify, request
from flask_cors import CORS
from game_logic import MemoryGame

app = Flask(__name__)
CORS(app)

# Initialize the game
game = MemoryGame()

@app.route('/shuffle', methods=['GET'])
def shuffle_cards():
    game.shuffle_cards()
    return jsonify({'cards': game.get_card_states()})

@app.route('/flip', methods=['POST'])
def flip_card():
    data = request.json
    index = data.get('index')
    if index is not None and isinstance(index, int):
        result = game.flip_card(index)
        return jsonify(result)
    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
