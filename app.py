from config import app
from views import views
from flask import request, jsonify
from main import Game

game = Game()

app.register_blueprint(views, url_prefix="/")

def get_game_info():
    try:
        game_dict = game.get_info()
        return jsonify({
            'current': game_dict['current'],
            'goal': game_dict['goal'],
            'options': list(game_dict['options']),
            'steps': game_dict['steps'],
            'length': game_dict['length']
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/start_game', methods=['POST'])
def start_game():
    try:
        diff = request.json.get('difficulty')
        game.reset()
        game.start_game(diff)
        return get_game_info()
    except Exception as e:
        return jsonify({'message': str(e)}), 500   

@app.route('/move_player', methods=['POST'])
def move_player():
    try:
        destination = request.json.get('dest')
        game.move(destination)
        return get_game_info()
    except Exception as e:
        return jsonify({'message': str(e)}), 500  

@app.route('/is_game_over', methods=['GET'])
def is_game_over():
    decision = None
    shortest_way = game.shortest_way()
    is_done = game.is_game_over()
    if (is_done):
        if game.has_won():
            decision = 'win'
        else:
            decision = 'lose'
    else:
        decision = 'continue'
    return jsonify({
        'decision' : decision,
        'shortest_way' : shortest_way
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
