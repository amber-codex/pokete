import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pokete_data.poketes import pokes
from pokete_data.attacks import attacks
from pokete import read_save


def test_rare_steini_defined():
    assert "rare_steini" in pokes


def test_rare_steini_in_deck():
    session_info = read_save()
    player_pokes = session_info.get("pokes", {})
    poke_names = [poke["name"] for poke in player_pokes.values()]
    assert "rare_steini" in poke_names


def test_attack_defined():
    assert "rock_and_roll" in attacks
