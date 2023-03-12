import tkinter as tk
from playsound import playsound

import controller
from tkinter import messagebox, font

import model
from Interface.setting_window import Settings

class Window:
    main_window: tk.Tk
    cell_button = []
    current_move = 0
    WIDTH = 0
    HEIGHT = 0
    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0
    SETTINGS = {}
    SOUND = r'C:\Users\17th\Desktop\XO Game\Interface\Click.wav'


    def __init__(self, settings):
        self.SETTINGS = settings
        self.main_window = tk.Tk()
        self.main_window.title('Крестики нолики')
        self.main_window.resizable(False, False)
        self.create_button()
        self.init_menu()
        self.main_window.update()
        self.WIDTH = self.main_window.winfo_reqwidth()
        self.HEIGHT = self.main_window.winfo_reqheight()
        self.SCREEN_WIDTH = (self.main_window.winfo_screenwidth() - self.WIDTH) // 2
        self.SCREEN_HEIGHT = (self.main_window.winfo_screenheight() - self.HEIGHT) // 2
        self.main_window.geometry(f'+{self.SCREEN_WIDTH}+{self.SCREEN_HEIGHT}')
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def press_button(self, index: int, mark: str):
        self.cell_button[index]['text'] = mark
        self.cell_button[index]['state'] = tk.DISABLED

    def init_menu(self):
        menu_bar = tk.Menu(self.main_window, tearoff=0)
        self.main_window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Новая игра', command=controller.new_game)
        file_menu.add_separator()
        file_menu.add_command(label='Настройки', command=self.window_settings)
        file_menu.add_separator()
        file_menu.add_command(label='Выйти', command=self.main_window.destroy)
        menu_bar.add_cascade(label='Игра', menu=file_menu)


    def get_current_move(self):
        return self.current_move

    def set_current_move(self, index: int):
        self.current_move = index

    def create_button(self):
        base_font = font.nametofont('TkDefaultFont')
        base_font_family = base_font.actual('family')
        base_font_size = int(base_font.actual('size'))
        header_font = font.Font(family=base_font_family,
                                size=base_font_size*4, weight='bold')
        k = 0
        for i in range(3):
            for j in range(3):
                cell_btn = tk.Button(self.main_window, text='', background='GRAY', font=header_font, disabledforeground='BLACK',
                                     height=2, width=6, command=lambda index=k: controller.playerTurn(index))
                self.cell_button.append(cell_btn)
                self.cell_button[k].grid(column=j, row=i )
                k += 1

    def refresh_button(self):
        for button in self.cell_button:
            button['text'] = ''
            button['state'] = tk.NORMAL
            button['background'] = "GRAY"
            button.update()
        self.main_window.update_idletasks()
        self.main_window.update()

    def win(self, win: tuple):
        for i in win:
            self.cell_button[i]['background'] = 'RED'

    def button_color(self,index: int, color: str):
        if color == 'X':
            self.cell_button[index]['background'] = self.SETTINGS.get("PLAYER_COLOR")
        else:
            self.cell_button[index]['background'] = self.SETTINGS.get("CPU_COLOR")

    def run(self):
        self.main_window.mainloop()
        model.save_settings()

    def window_settings(self):
        self.win_set = Settings(self.main_window, self.SETTINGS)

    def on_closing(self):
        if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
            model.save_settings()
            self.main_window.destroy()

    def clicked_sound(self):
        playsound(self.SOUND, block=False)