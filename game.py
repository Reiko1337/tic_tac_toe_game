import random
import numpy as np
from prettytable import PrettyTable, ALL


class BasePlayer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class PlayerTicTacToe(BasePlayer):
    def __init__(self, name: str, cross: bool = True):
        super().__init__(name)
        self.cross = cross

    def get_symbol(self) -> str:
        return 'X' if self.cross else '0'


class SessionGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1 = PlayerTicTacToe(player1_name)
        self.player2 = PlayerTicTacToe(player2_name, cross=False)
        self.players = [self.player1, self.player2]

    def get_session_player(self):
        _player = self.players.pop(0)
        self.players.append(_player)
        return _player

    def get_session(self):
        random.shuffle(self.players)
        return self.players


class TicTacToeGame:
    def __init__(self, session: SessionGame):
        self.session = session
        self.area = np.array([
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ])
        self.game_area = PrettyTable()
        self.game_area.header = False
        self.game_area.hrules = ALL
        self.game_area.padding_width = 2

        self.__x = None
        self.__y = None

    def print_game_area(self):
        self.game_area.clear_rows()
        self.game_area.add_rows(self.area)
        print(self.game_area)

    def check_win(self, player: PlayerTicTacToe) -> bool:
        _symbol = player.get_symbol()
        coordinates_diag = (
            (0, 0), (1, 1), (2, 2), (0, 2), (2, 0)
        )
        if (self.__x, self.__y) in coordinates_diag and (
                tuple(self.area.diagonal()).count(_symbol) == 3 or tuple(np.fliplr(self.area).diagonal()).count(
            _symbol) == 3):
            return True
        elif tuple(self.area[self.__x]).count(_symbol) == 3 or tuple(self.area[:, self.__y]).count(_symbol) == 3:
            return True
        else:
            return False

    def check_value(self) -> bool:
        accept_value = []
        for i in range(3):
            for j in range(3):
                if self.area[i, j] == ' ':
                    accept_value.append((i, j))

        if (self.__x, self.__y) not in accept_value:
            return False
        return True

    def set_value(self, player: PlayerTicTacToe):
        _symbol = player.get_symbol()
        self.area[self.__x, self.__y] = _symbol

    def input_coordinates(self, player):
        try:
            self.__x, self.__y = map(lambda value: int(value) - 1, input(f'Ход игрока {player.name}: ').split())
            return self.check_value()
        except ValueError:
            return False

    def start(self):
        print('--Игра начинается--\n')
        while True:
            self.print_game_area()
            player = self.session.get_session_player()
            while True:
                if self.input_coordinates(player):
                    self.set_value(player)
                    break
                print('Неверное значение. Попробуйте еще. \n')
            if self.check_win(player):
                break
        print(f'Игра окончена! Победитель: {player.name}')
