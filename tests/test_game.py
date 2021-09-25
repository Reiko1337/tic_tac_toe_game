import pytest
import numpy as np
from game import TicTacToeGame, PlayerTicTacToe
from .test_session import get_session_fixture


@pytest.fixture
def get_game_area():
    area = np.array([
        ['X', ' ', 'X'],
        [' ', '0', ' '],
        ['0', 'x', ' ']
    ])
    return area


@pytest.fixture
def get_game(get_session_fixture):
    session = get_session_fixture
    return TicTacToeGame(session)


@pytest.fixture
def get_game_with_custom_game_area(get_game_area, get_game):
    game = get_game
    game.area = get_game_area
    return game


def test_valid_value_input_coordinates(get_game, monkeypatch):
    player = PlayerTicTacToe('test_player_1')
    game = get_game
    monkeypatch.setattr('builtins.input', lambda _: "11")
    assert game.input_coordinates(player) is False
    monkeypatch.setattr('builtins.input', lambda _: "cz   1 1 ")
    assert game.input_coordinates(player) is False
    monkeypatch.setattr('builtins.input', lambda _: "3 3 1")
    assert game.input_coordinates(player) is False
    monkeypatch.setattr('builtins.input', lambda _: "3 3")
    assert game.input_coordinates(player) is True


def test_check_value_by_input_coordinates(get_game_with_custom_game_area, monkeypatch):
    player = PlayerTicTacToe('test_player_1')
    game = get_game_with_custom_game_area
    monkeypatch.setattr('builtins.input', lambda _: "1 1")
    assert game.input_coordinates(player) is False
    monkeypatch.setattr('builtins.input', lambda _: "2 1")
    assert game.input_coordinates(player) is True
    monkeypatch.setattr('builtins.input', lambda _: "4 4")
    assert game.input_coordinates(player) is False


def test_set_value(get_game, monkeypatch):
    player = PlayerTicTacToe('test_player_1')
    game = get_game
    monkeypatch.setattr('builtins.input', lambda _: "1 3")
    game.input_coordinates(player)
    game.set_value(player)
    assert np.array_equal(game.area, np.array([
        [' ', ' ', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]))


def test_check_win(get_game_with_custom_game_area, monkeypatch):
    player_1 = PlayerTicTacToe('test_player_1')
    player_2 = PlayerTicTacToe('test_player_2', cross=False)
    game = get_game_with_custom_game_area
    monkeypatch.setattr('builtins.input', lambda _: "1 2")
    game.input_coordinates(player_1)
    game.set_value(player_1)
    assert game.check_win(player_1) is True
    game = get_game_with_custom_game_area
    game.set_value(player_2)
    assert game.check_win(player_1) is False