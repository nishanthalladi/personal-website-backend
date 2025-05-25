from stockfish import Stockfish

# Use the default path for systems with stockfish installed via apt (e.g. Dockerfile setup)
stockfish = Stockfish(path="/usr/games/stockfish")
# stockfish = Stockfish(path="/Users/nishu/Local/chess/stockfish/stockfish")
stockfish.set_skill_level(20)

def get_drawish_move_from_fen(fen_string: str) -> dict:
    try:
        stockfish.set_fen_position(fen_string)
        top_moves = stockfish.get_top_moves(10)
        drawish_moves = []

        for move in top_moves:
            if "Centipawn" in move and move["Centipawn"] is not None:
                eval_score = abs(move["Centipawn"])
            elif "Mate" in move and move["Mate"] is not None:
                # Treat mate scores as highly decisive to avoid them
                eval_score = 10000
            else:
                continue  # skip if neither evaluation is present
            drawish_moves.append((move["Move"], eval_score))

        drawish_moves.sort(key=lambda x: x[1])
        best_drawish = drawish_moves[0][0] if drawish_moves else None

        if best_drawish and len(best_drawish) >= 4:
            return {
                'from': best_drawish[:2],
                'to': best_drawish[2:4],
                'uci': best_drawish
            }
        return {
            'from': None,
            'to': None,
            'uci': None
        }
    except Exception as e:
        return {
            'error': str(e)
        }
