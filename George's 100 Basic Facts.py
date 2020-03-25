from tkinter import *
import tkinter.ttk as ttk
import random as rnd
import time

class main_window():
    def __init__(self):
        self.main_menu()
        
        #Styles for the menu options
        butt_style = ttk.Style()
        butt_style.configure("big.TButton", font=("Arial", 25, "bold"))

        extra_big_field = ttk.Style()
        extra_big_field.configure("extra_big.TEntry", font=("Arial", 45))

        drop_style = ttk.Style()
        drop_style.configure("big.TMenubutton", font=("Arial", 10, "bold"))

        check_style = ttk.Style()
        check_style.configure("bg.TCheckbutton", background="#2c3f85", foreground="white", font=("Arial",11,"bold"))

    def main_menu(self):
        try:        #Clear the other sections if they exist
            self.instructions.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:
            self.highscores.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:
            self.basic_facts.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:        
            window.geometry("400x400")
            self.menu = Frame(window, width=390, height=390, bg="#2c3f85")
            self.menu.grid(row=0,column=0,padx=5,pady=5)
            self.menu.grid_propagate(False)
            self.menu.grid_columnconfigure(0,weight=1)
            self.menu.grid_columnconfigure(1,weight=1)
            Label(self.menu, text="George's 100 Basic Facts", bg="#2c3f85", fg="white", font="Bahnschrift 25 bold").grid(row=0, column=0, columnspan=2, pady=15)


            #Start and highscore buttons
            self.Start_Button = ttk.Button(self.menu, text="Start", command=lambda:self.play(), width=7, style="big.TButton")
            self.Start_Button.grid(row=1,column=0,pady=20)
            ttk.Button(self.menu, text="Highscores", command=lambda:self.show_highscores()).grid(row=1,column=1,pady=20)
            ttk.Button(self.menu, text="Instructions", command=lambda:self.show_instructions()).grid(row=2,column=1,pady=20)

            #Difficulty Dropdown
            self.difficulty_value = StringVar()
            self.difficulty = ttk.OptionMenu(self.menu, self.difficulty_value, "Difficulty","Easy","Medium","Hard","Expert", style="big.TMenubutton")
            self.difficulty.config(width=10)
            self.difficulty.grid(row=2,column=0,pady=20)

            #Checkbuttons to selection functions
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

    def show_instructions(self):
        try:        #Clear the other menu if it exists
            self.menu.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:
            pass
        
    def play(self):
        try:        #Clear the other menu if it exists
            self.menu.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:
            generate_problems(self.difficulty_value.get(), self.add_var.get(), self.sub_var.get(), self.mult_var.get(), self.div_var.get())

            self.basic_facts = Frame(window, width=390, height=390, bg="#86e0dd")
            self.basic_facts.grid(row=0,column=0,padx=5,pady=5)
            self.basic_facts.grid_propagate(False)
            self.basic_facts.grid_columnconfigure(0,weight=1)
            self.basic_facts.grid_columnconfigure(1,weight=1)
            self.basic_facts.grid_columnconfigure(2,weight=1)
            self.basic_facts.grid_rowconfigure(0,weight=1)
            self.basic_facts.grid_rowconfigure(1,weight=1)
            self.basic_facts.grid_rowconfigure(2,weight=1)

            question_var.set("Hello")


            Label(self.basic_facts, textvariable=question_var, bg="#86e0dd", fg="black", font=("Arial", 65, "bold")).grid(row=0,column=1)
            self.answer_box = ttk.Entry(self.basic_facts, textvariable=answer, style="extra_big.TEntry", font=("Arial",20)).grid(row=1,column=1)

            
    def show_highscores(self):
        try:        #Clear the other menu if it exists
            self.menu.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:
            pass

def next_question():
    pass


def generate_problems(difficulty="Medium", add=True, sub=True, mult=True, div=True):        #Generates problems according to the formula laid out in Problem Difficulty Explanation.xlsx
    selected_functions=[]
    if difficulty == "Difficulty": difficulty = "Medium"
    selected_functions.clear()
    problem_list.clear()
    if add: selected_functions.append("add")
    if sub: selected_functions.append("sub")
    if mult: selected_functions.append("mult")
    if div: selected_functions.append("div")
    for i in range(100):
        num_1 = 0
        num_2 = 0
        current_operation = (rnd.choice(selected_functions))
        if current_operation == "add":
            if difficulty == "Easy":
                num_1 = rnd.randint(1,9)
                num_2 = rnd.randint(1,9)
            elif difficulty == "Medium":
                num_1 = rnd.randint(1,9)
                num_2 = rnd.randint(10,99)
            elif difficulty == "Hard":
                num_1 = rnd.randint(1,9) * int(rnd.choice([2,5,10]))
                num_2 = rnd.randint(10,99)
            elif difficulty == "Expert":
                num_1 = rnd.randint(10,99)
                num_2 = rnd.randint(10,99)
            full_problem = str(num_1) +  " + " + str(num_2)
            problem_list.append(full_problem)
        elif current_operation == "sub":
            while num_1 == num_2:
                if difficulty == "Easy":
                    num_1 = rnd.randint(1,9)
                    num_2 = rnd.randint(1,9)
                elif difficulty == "Medium":
                    num_1 = rnd.randint(1,9)
                    num_2 = rnd.randint(10,99)
                elif difficulty == "Hard":
                    num_1 = rnd.randint(1,9) * int(rnd.choice([2,5,10]))
                    num_2 = rnd.randint(10,99)
                elif difficulty == "Expert":
                    num_1 = rnd.randint(10,99)
                    num_2 = rnd.randint(10,99)
            if num_1 > num_2:
                full_problem = str(num_1) +  " - " + str(num_2)
            else:
                full_problem = str(num_2) +  " - " + str(num_1)
            problem_list.append(full_problem)        
        elif current_operation == "mult":
            if difficulty == "Easy":
                num_1 = int(rnd.choice([2,5,10]))
            elif difficulty == "Medium":
                num_1 = int(rnd.choice([2,5,10,4,3,9]))
            elif difficulty == "Hard":
                num_1 = int(rnd.choice([2,5,10,4,3,9,11,6,8]))
            elif difficulty == "Expert":
                num_1 = rnd.randint(2,12)
            num_2 = rnd.randint(2,12)
            full_problem = str(num_1) +  " x " + str(num_2)
            problem_list.append(full_problem)        
        elif current_operation == "div":
            if difficulty == "Easy":
                num_1 = int(rnd.choice([2,5,10]))
            elif difficulty == "Medium":
                num_1 = int(rnd.choice([2,5,10,4,3,9]))
            elif difficulty == "Hard":
                num_1 = int(rnd.choice([2,5,10,4,3,9,11,6,8]))
            elif difficulty == "Expert":
                num_1 = rnd.randint(2,12)
            num_2 = rnd.randint(2,12)
            full_problem = str(num_1*num_2) + " ÷ " + str(num_1)
            problem_list.append(full_problem)

#Accuracy/Time
#Or perhaps dock time
            
window = Tk()

problem_list=[]
question_var = StringVar()
answer = StringVar()

main_window()
