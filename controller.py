import random

import bot
import model
from Classes import Board
from Interface.main_window import Window

from tkinter import messagebox

main_window : Window
board : Board.Board

def intro():
    global main_window
    global board
    model.load_settings()
    board = Board.Board(model.get_settings())
    main_window = Window(model.get_settings())
    if board.getMark() == 'R':
        board.setMark(random.choice(['X', 'O']))
    if board.getMark() == 'O':
        enemyTurn()
    main_window.run()

def new_game():
    main_window.refresh_button(model.get_settings())
    board.new_game(model.get_settings())
    if board.getMark() == 'R':
        board.setMark(random.choice(['X', 'O']))
    if board.getMark() == 'O':
        enemyTurn()


def playerTurn(index):
    global board
    board.setBoard(index)
    mark = board.getMark()
    main_window.button_color(index, mark)
    main_window.press_button(index, mark)
    # main_window.clicked_sound()
    if board.win_condition():
        main_window.win(board.win_condition())
        if messagebox.askyesno('Победа!', 'Терминатор соснул!'):
            new_game()
        else:
            main_window.main_window.destroy()
        enemyTurn()
    board.changeMark()
    if board.check_tie():
        if messagebox.askyesno('Ничья!', 'Вы оба облажались!'):
            new_game()
        else:
            main_window.main_window.destroy()
    else:
        enemyTurn()

def enemyTurn():
    global board
    mark = board.getMark()
    move = bot.AIMove(board)
    main_window.press_button(move, mark)
    main_window.button_color(move, mark)
    # main_window.clicked_sound()
    board.setBoard(move)
    board.changeMark()
    if board.win_condition():
        main_window.win(board.win_condition())
        if messagebox.askyesno('Поражение...', 'Ты проиграл, победа за желязякой'):
            new_game()
        else:
            main_window.main_window.destroy()
        return
    if board.check_tie():
        if messagebox.askyesno('Ничья!', 'Вы оба облажались!'):
            new_game()
        else:
            main_window.main_window.destroy()
