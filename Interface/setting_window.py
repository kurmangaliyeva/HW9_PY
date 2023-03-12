import random
import tkinter as tk

import controller
from tkinter import colorchooser, ttk


class Settings():
    win_set: tk.Toplevel
    cell_button = []
    current_move = 0
    WIDTH = 0
    HEIGHT = 0
    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0
    SETTINGS = {}
    PARRENT : tk.Tk


    def __init__(self, main_window, settings):
        self.PARRENT = main_window
        self.SETTINGS = settings
        self.PLAYER_COLOR = settings.get('PLAYER_COLOR')
        self.CPU_COLOR = settings.get('CPU_COLOR')
        self.win_set = tk.Toplevel(main_window)
        self.win_set.title('Настойки')
        self.win_set.resizable(False, False)
        self.WIDTH = 200
        self.HEIGHT = 200
        self.SCREEN_WIDTH = (self.win_set.winfo_screenwidth() - self.WIDTH) // 2
        self.SCREEN_HEIGHT = (self.win_set.winfo_screenheight() - self.HEIGHT) // 2
        self.win_set.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.SCREEN_WIDTH}+{self.SCREEN_HEIGHT}')
        self.win_set.wm_attributes("-topmost", 1)


        self.btn_player_color = tk.Button(self.win_set, text='Выбрать цвет игрока', height=1, width=30,
                                          background=self.PLAYER_COLOR, command=self.choose_player_color)
        self.btn_player_color.pack()
        self.btn_cpu_color = tk.Button(self.win_set, text='Выбрать цвет бота', height=1, width=30, background=self.CPU_COLOR,
                                       command=self.choose_cpu_color)
        self.btn_cpu_color.pack()

        mark_x = "X"
        mark_o = "O"
        mark_r = 'R'
        self.choose_mark = tk.StringVar(value=mark_x if self.SETTINGS.get('PLAYER_MARK') == "X" else mark_o)
        radio_x = ttk.Radiobutton(self.win_set, text='Играем за крестики', value=mark_x, variable=self.choose_mark)
        radio_o = ttk.Radiobutton(self.win_set, text='Играем за нолики', value=mark_o, variable=self.choose_mark)
        radio_r = ttk.Radiobutton(self.win_set, text='Играем за рандом', value=mark_r, variable=self.choose_mark)
        radio_x.pack()
        radio_o.pack()
        radio_r.pack()

        btn_confirm = tk.Button(self.win_set, text='Применить', width=20, command=self.apply_settings)
        btn_confirm.pack()


    def choose_player_color(self):
        self.win_set.wm_attributes("-topmost", 0)
        color_code = colorchooser.askcolor(title="Choose color")
        self.PLAYER_COLOR = color_code[1]
        self.win_set.wm_attributes("-topmost", 1)
        self.btn_player_color['background'] = self.PLAYER_COLOR


    def choose_cpu_color(self):
        self.win_set.wm_attributes("-topmost", 0)
        color_code = colorchooser.askcolor(title="Choose color", )
        self.CPU_COLOR = color_code[1]
        self.win_set.wm_attributes("-topmost", 1)
        self.btn_cpu_color['background'] = self.CPU_COLOR

    def apply_settings(self):
        self.SETTINGS['PLAYER_COLOR'] = self.PLAYER_COLOR
        self.SETTINGS['CPU_COLOR'] = self.CPU_COLOR
        self.SETTINGS['PLAYER_MARK'] = self.choose_mark.get()
        controller.new_game()
        self.PARRENT.focus_set()
        self.win_set.destroy()