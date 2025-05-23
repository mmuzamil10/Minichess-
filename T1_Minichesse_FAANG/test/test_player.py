
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'T2_Minichess_Game')))

from player import Player

def test_convert_to_index_valid():
    p = Player("Tester", "W")
    assert p.convert_to_index("a2") == (6, 0)
    assert p.convert_to_index("h1") == (7, 7)

def test_convert_to_index_invalid():
    p = Player("Tester", "W")
    with pytest.raises(ValueError):
        p.convert_to_index("z9")

def test_is_within_bounds():
    p = Player("Tester", "W")
    assert p.is_within_bounds((0, 0))
    assert not p.is_within_bounds((8, 8))
