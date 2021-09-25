from game import PlayerTicTacToe


def test_get_symbol_x():
    player = PlayerTicTacToe('test_player')
    assert player.get_symbol() == 'X'


def test_get_symbol_0():
    player = PlayerTicTacToe('test_player', cross=False)
    assert player.get_symbol() == '0'
