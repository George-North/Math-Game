from tkinter import *
import tkinter.ttk as ttk
import time

class main_window():
    def __init__(self):
        window.geometry("400x400")
        self.menu = Frame(window, width=390, height=390, bg="#2c3f85")
        self.menu.grid(row=0,column=0,padx=5,pady=5)
        self.menu.grid_propagate(False)
        self.menu.grid_columnconfigure(0,weight=1)
        self.menu.grid_columnconfigure(1,weight=1)
        Label(self.menu, text="George's Basic Facts", bg="#2c3f85", fg="white", font="Bahnschrift 25 bold").grid(row=0, column=0, columnspan=2, pady=15)

        ttk.Button(self.menu, text="Start", command=lambda:basic_facts()).grid(row=1,column=0)
        ttk.Button(self.menu, text="Highscores", command=lambda:highscores()).grid(row=1,column=1)

        
        
        
    def basic_facts(self):
        pass

    def highscores(self):
        pass



window = Tk()
main_window()
