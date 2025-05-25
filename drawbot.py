import requests

def get_drawish_move_from_lichess(fen_string: str) -> dict:
    url = f"https://lichess.org/api/cloud-eval?fen={fen_string}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        move_str = result.get('pvs', [{}])[0].get('moves', '').split()[0] if result.get('pvs') else None

        if move_str and len(move_str) >= 4:
            return {
                'from': move_str[:2],
                'to': move_str[2:4],
                'uci': move_str
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
    

