import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from drawbot import get_drawish_move_from_lichess

def test_valid_fen():
    fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"  # After 1. e4
    result = get_drawish_move_from_lichess(fen)
    assert 'from' in result and 'to' in result and 'uci' in result
    assert result['from'] is not None
    assert result['to'] is not None
    assert len(result['uci']) >= 4

def test_invalid_fen():
    fen = "invalid-fen-string"
    result = get_drawish_move_from_lichess(fen)
    assert 'error' in result

def test_missing_move():
    # This is a rare or contrived example; empty board likely yields no move
    fen = "8/8/8/8/8/8/8/8 w - - 0 1"
    result = get_drawish_move_from_lichess(fen)
    assert 'uci' not in result or result['uci'] is None