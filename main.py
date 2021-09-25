from game import TicTacToeGame, SessionGame

if __name__ == '__main__':
    player1_name = input('Игрок #1 (X), Ваше имя: ')
    player2_name = input('Игрок #2 (0), Ваше имя: ')
    session = SessionGame(player1_name, player2_name)
    game = TicTacToeGame(session)
    game.start()
