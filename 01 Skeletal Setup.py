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

        butt_style = ttk.Style()
        butt_style.configure("big.TButton", font=("Arial", 25, "bold"))

        drop_style = ttk.Style()
        drop_style.configure("big.TMenubutton", font=("Arial", 10, "bold"))

        check_style = ttk.Style()
        check_style.configure("bg.TCheckbutton", background="#2c3f85", foreground="white", font=("Arial",11,"bold"))
        

        self.Start_Button = ttk.Button(self.menu, text="Start", command=lambda:self.basic_facts(), width=7, style="big.TButton")
        self.Start_Button.grid(row=1,column=0,pady=20)
        ttk.Button(self.menu, text="Highscores", command=lambda:self.highscores()).grid(row=1,column=1,pady=20)

        self.difficulty_value = StringVar()
        self.difficulty = ttk.OptionMenu(self.menu, self.difficulty_value, "Difficulty","Easy","Medium","Hard","Expert", style="big.TMenubutton")
        self.difficulty.config(width=10)
        self.difficulty.grid(row=2,column=0,pady=20)

        self.add_var = BooleanVar(value=True)
        self.add = ttk.Checkbutton(self.menu, variable=self.add_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Addition")
        self.add.grid(row=3,column=0,pady=20)
        
        self.sub_var = BooleanVar(value=True)
        self.subtract = ttk.Checkbutton(self.menu, variable=self.sub_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Subtraction")
        self.subtract.grid(row=4,column=0,pady=20)
        
        self.mult_var = BooleanVar(value=True)
        self.multiply = ttk.Checkbutton(self.menu, variable=self.mult_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Multiplication")
        self.multiply.grid(row=3,column=1,pady=20)
        
        self.div_var = BooleanVar(value=True)
        self.divide = ttk.Checkbutton(self.menu, variable=self.div_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Division")
        self.divide.grid(row=4,column=1,pady=20)

    def an_option(self):
        if self.add_var.get()==False and self.sub_var.get()==False and self.mult_var.get()==False and self.div_var.get()==False:
            self.Start_Button.config(state=DISABLED)
        else:
            self.Start_Button.config(state=NORMAL)
        
        
    def basic_facts(self):
        pass

    def highscores(self):
        pass



window = Tk()
main_window()
