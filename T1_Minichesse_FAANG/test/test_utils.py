import sys
import os

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'T2_Minichess_Game')))

from utils import algebraic_to_index, index_to_algebraic


def test_algebraic_to_index():
    assert algebraic_to_index("a2") == (6, 0)
    assert algebraic_to_index("h8") == (0, 7)

def test_index_to_algebraic():
    assert index_to_algebraic((6, 0)) == "a2"
    assert index_to_algebraic((0, 7)) == "h8"

def test_algebraic_to_index_invalid():
    with pytest.raises(ValueError):
        algebraic_to_index("z9")
