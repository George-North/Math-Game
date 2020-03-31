from tkinter import *
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import random as rnd
import time as t

class main_window():
    def __init__(self):
        self.main_menu()
        
        #Styles for the menu options
        butt_style = ttk.Style()
        butt_style.configure("big.TButton", font=("Arial", 27, "bold"))

        normal_butt_style = ttk.Style()
        normal_butt_style.configure("normal.TButton", font=12)

        drop_style = ttk.Style()
        drop_style.configure("big.TMenubutton", font=("Arial", 12, "bold"))

        check_style = ttk.Style()
        check_style.configure("bg.TCheckbutton", background="#2c3f85", foreground="white", font=("Arial",14,"bold"))

        green_check_style = ttk.Style()
        green_check_style.configure("green_bg.TCheckbutton", background="#32cd32", font=("Arial", 11, "bold"))

    def main_menu(self):    #Make the Menu
        try:        #Clear the other sections if they exist
            self.instructions.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:
            self.highscore_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:
            self.results_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:        
            self.menu_page = Frame(window, width=490, height=490, bg="#2c3f85")     #Lay out the background
            self.menu_page.grid(row=0,column=0,padx=5,pady=5)
            self.menu_page.grid_propagate(False)                            #Fill the background so it doesn't stick tight to the widgets
            self.menu_page.grid_columnconfigure(0,weight=1)                 #Evenly space the columns and rows
            self.menu_page.grid_columnconfigure(1,weight=1)

            Label(self.menu_page, text="George's 100 Basic Facts", bg="#2c3f85", fg="white", font="Bahnschrift 30 bold").grid(row=0, column=0, columnspan=2, pady=25)


            #Start and highscore buttons
            self.Start_Button = ttk.Button(self.menu_page, text="Start", command=self.play, width=7, style="big.TButton")
            self.Start_Button.grid(row=1,column=0,pady=25)
            ttk.Button(self.menu_page, text="Highscores", command=self.show_highscores, style="normal.TButton").grid(row=1,column=1,pady=25)
            ttk.Button(self.menu_page, text="Instructions", command=self.show_instructions, style="normal.TButton").grid(row=2,column=1,pady=25)

            #Difficulty Dropdown
            self.difficulty_value = StringVar()
            self.difficulty = ttk.OptionMenu(self.menu_page, self.difficulty_value, "Difficulty","Easy","Medium","Hard","Expert", style="big.TMenubutton")
            self.difficulty.config(width=10)
            self.difficulty.grid(row=2,column=0,pady=25)

            #Checkbuttons to select functions
            self.add_var = BooleanVar(value=True)
            self.add = ttk.Checkbutton(self.menu_page, variable=self.add_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Addition")
            self.add.grid(row=3,column=0,pady=25)
            
            self.sub_var = BooleanVar(value=True)
            self.subtract = ttk.Checkbutton(self.menu_page, variable=self.sub_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Subtraction")
            self.subtract.grid(row=4,column=0,pady=25)
            
            self.mult_var = BooleanVar(value=True)
            self.multiply = ttk.Checkbutton(self.menu_page, variable=self.mult_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Multiplication")
            self.multiply.grid(row=3,column=1,pady=25)
            
            self.div_var = BooleanVar(value=True)
            self.divide = ttk.Checkbutton(self.menu_page, variable=self.div_var, command=self.an_option, width=13, style="bg.TCheckbutton", text="Division")
            self.divide.grid(row=4,column=1,pady=25)

    def show_instructions(self):    #Explains how to play
        try:        #Clear the other menu if it exists
            self.menu_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:
            self.instructions_page = Frame(window, bg="#8009bc", width=490, height=490)     #Lay out the background
            self.instructions_page.grid(row=0,column=0,pady=5,padx=5)
            self.instructions_page.grid_propagate(False)                            #Fill the background so it doesn't stick tight to the widgets

            Label(self.instructions_page, text=instruction_text, bg="#8009bc", fg="white", justify=LEFT, font=("Arial", 16, "bold"), wraplength=480).grid(row=0,column=0, pady=5,padx=5)
            ttk.Button(self.instructions_page, command=self.main_menu, text="Main Menu").grid(row=1,column=0, pady=25)      #Back to the main menu
        
    def play(self): #Where the user can answer questions
        global question_number
        global start_time
        try:        #Clear the other menu if it exists
            self.menu_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:        #Clear the other menu if it exists
            self.results_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        finally:
            generate_problems(self.difficulty_value.get(), self.add_var.get(), self.sub_var.get(), self.mult_var.get(), self.div_var.get())     #Make the problems

            self.basic_facts = Frame(window, width=490, height=490, bg="#86e0dd")     #Lay out the background
            self.basic_facts.grid(row=0,column=0,padx=5,pady=5)
            self.basic_facts.grid_propagate(False)                            #Fill the background so it doesn't stick tight to the widgets
            for i in range(3):
                self.basic_facts.grid_columnconfigure(i,weight=1)                 #Evenly space the columns and rows
                self.basic_facts.grid_rowconfigure(i,weight=1)
    
            question_number=0                   #Reset the variables so the user can play multiple times
            user_answer_list.clear()
            question_var.set(problem_list[question_number])
            
            window.bind("<Return>", self.next_question)     #Allows the user to press enter to move to the next question

            self.question = Label(self.basic_facts, textvariable=question_var, bg="#86e0dd", fg="black", font=("Arial", 65, "bold"))
            self.question.grid(row=0,column=1)
            self.answer_box = ttk.Entry(self.basic_facts, textvariable=answer, font=("Arial 45"), width=10, validate="key")
            self.answer_box['validatecommand'] = (self.answer_box.register(is_num),'%P','%d')               #Only lets the user make approved (number) entries
            self.answer_box.grid(row=1,column=1)
            
            start_time = t.time()       #Gets the time now

    def results(self):  #Shows the results
        global duration
        global question_number
        global score
        duration = t.time() - start_time        #Calculates how long the user took
        self.basic_facts.grid_forget()          #Clear the old window
        self.results_page = Frame(window, width=490, height=490, bg="#6b6b6b")     #Lay out the background
        self.results_page.grid(row=0,column=0,padx=5,pady=5)
        for i in range(4):
            self.results_page.grid_columnconfigure(i,weight=1)                 #Evenly space the columns and rows
        for i in range(5):
            self.results_page.grid_rowconfigure(i,weight=1)
        self.results_page.grid_propagate(False)                            #Fill the background so it doesn't stick tight to the widgets
        score=0

        init1=""
        init2=""
        init3=""

        self.output_box=scrolledtext.ScrolledText(self.results_page,height=20,width=40,font="Arial 12 bold")        #Makes a box so the user can look through their answers
        self.output_box.grid(row=1, column=0, columnspan=3, rowspan=3)
        
        self.output_box.tag_config("Correct", background="green")       #Colours the rows
        self.output_box.tag_config("Wrong", background="Red")
       
        self.output_box.insert("end", "Question         Your Answer         Correct Answer\n")

        self.output_box.configure(state="normal")
        
        for i in range(len(user_answer_list)):      #Marks the answers
            x = user_answer_list[i]         #Sure wish I knew why I had to do it this way
            y = correct_answer_list[i]
            line = str(problem_list[i]) + "                              " + str(x) + "                            " + str(y) + "\n"
            if x == y:
                self.output_box.insert("end", line, "Correct")
                score += 1
            else:
                self.output_box.insert("end", line, "Wrong")
            
        self.output_box.configure(state="disabled")         #Prevents the user editing the comments
                
        header = str("You Got: " + str(score) + "/100 in " + str(round(duration, 1)) + "s")
        Label(self.results_page, text=header, bg="#6b6b6b", fg="white", font="Bahnschrift 25 bold").grid(row=0, column=0, columnspan=3, pady=10)
        
        ttk.Button(self.results_page, text="Save Results", command=self.save_results).grid(row=0,column=4,pady=15, padx=(0,12)) 
        ttk.Button(self.results_page, text="Play Again", command=self.play).grid(row=1,column=4,pady=15, padx=(0,12))
        ttk.Button(self.results_page, text="Highscores", command=self.show_highscores).grid(row=2,column=4,pady=15, padx=(0,12))
        ttk.Button(self.results_page, text="Main Menu", command=self.main_menu).grid(row=3,column=4,pady=15, padx=(0,12))
                
    def save_results(self):     #Allows the user to save their initials to the highscore
        self.results_page.grid_forget()
        self.save_page = Frame(window, width=490, height=490, bg="#f4732e")     #Lay out the background
        self.save_page.grid(row=0,column=0, padx=5, pady=5)
        for i in range(3):
            self.save_page.grid_columnconfigure(i,weight=1)                 #Evenly space the columns and rows
        for i in range(4):
            self.save_page.grid_rowconfigure(i,weight=1)                    #Fill the background so it doesn't stick tight to the widgets
        self.save_page.grid_propagate(False)

        Label(self.save_page, text="Enter Initials", font="Bahnschrift 45 bold", bg="#f4732e", fg="Black").grid(row=0,column=0,columnspan=3)

        self.box_1 = ttk.Entry(self.save_page, textvariable=init_1, font=("Arial 45"), width=2, validate="key")
        self.box_1.grid(row=1,column=0)
        self.box_1['validatecommand'] = (self.box_1.register(one_char),'%P','%d')           #Only lets the user enter approved characters (1 character alphanumeric)
        self.box_2 = ttk.Entry(self.save_page, textvariable=init_2, font=("Arial 45"), width=2, validate="key")
        self.box_2.grid(row=1,column=1)
        self.box_2['validatecommand'] = (self.box_1.register(one_char),'%P','%d')           #Only lets the user enter approved characters (1 character alphanumeric)
        self.box_3 = ttk.Entry(self.save_page, textvariable=init_3, font=("Arial 45"), width=2, validate="key")
        self.box_3.grid(row=1,column=2)
        self.box_3['validatecommand'] = (self.box_3.register(one_char),'%P','%d')           #Only lets the user enter approved characters (1 character alphanumeric)

        ttk.Button(self.save_page, text="Save", command=lambda:self.save(self.box_1.get(), self.box_2.get(), self.box_3.get()), style="big.TButton").grid(row=2,column=1) 
        ttk.Button(self.results_page, text="Main Menu", command=self.main_menu).grid(row=3,column=2,pady=15)

    def an_option(self):    #Only allows the user to start if they have selected at least one operation (on the main menu)
        if self.add_var.get()==False and self.sub_var.get()==False and self.mult_var.get()==False and self.div_var.get()==False:
            self.Start_Button.config(state=DISABLED)
        else:
            self.Start_Button.config(state=NORMAL)

    def save(self,char1,char2,char3):        #Write to the file and take the user to the main menu
        name = char1 + char2 + char3
        if char1 != "" and char2 != "" and char3 != "":     #Only lets them save if they've entered something in all 3 fields
            val = round(calc_score(),2)
            with open("Highscores.txt", "r+") as highscore_file:        #Opens the file
                for line in highscore_file:
                    highscore_list.append(line)        
                highscore_file.truncate(0)  #Wipes the file
                highscore_file.seek(0)      #Resets the write head to the start of the file
                difficulty = self.difficulty_value.get()
                if difficulty == "Difficulty": difficulty = "Medium"
                l = str(val) + "," + name + "," + str(difficulty) + "," + str(self.add_var.get()) + "," + str(self.sub_var.get()) + "," + str(self.mult_var.get()) + "," + str(self.div_var.get()) + "\n"
                highscore_list.append(l)
                for i in highscore_list:
                    highscore_file.write(i)     #Writes to the file
            self.save_page.grid_forget()
            self.main_menu()
                            #Because I'm using with it automatically handles flushing and closing the file
        
            
    def show_highscores(self):      #Allows the user to browse highscores that match the filters they apply on the right
        try:        #Clear the other menu if it exists
            self.menu_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        try:        #Clear the other menu if it exists
            self.results_page.grid_forget()
        except AttributeError:  #Stops the error message being printed
            pass
        
        finally:
            self.highscore_page = Frame(window, bg="#32cd32", width=490, height=490)
            self.highscore_page.grid(row=0,column=0,pady=5,padx=5)

            for i in range(4):
                self.highscore_page.grid_columnconfigure(i,weight=1)
            for i in range(5):
                self.highscore_page.grid_rowconfigure(i,weight=1)
            self.highscore_page.grid_propagate(False)

            
            Label(self.highscore_page, text="Highscores", font="Bahnschrift 30 bold", bg="#32cd32").grid(row=0,column=0,columnspan=2)
            ttk.Button(self.highscore_page, text="Main Menu", command=self.main_menu).grid(row=0,column=2)

            #Difficulty Dropdown
            self.highscore_difficulty_value = StringVar()
            self.highscore_difficulty = ttk.OptionMenu(self.highscore_page, self.highscore_difficulty_value, "Difficulty","Easy","Medium","Hard","Expert", command=self.search_highscores)
            self.highscore_difficulty.config(width=10)
            self.highscore_difficulty.grid(row=0,column=3)

            #Checkbuttons to select functions
            self.highscore_add_var = BooleanVar(value=True)
            self.highscore_add = ttk.Checkbutton(self.highscore_page, variable=self.highscore_add_var, width=13, command=self.search_highscores, text="Addition", style="green_bg.TCheckbutton")
            self.highscore_add.grid(row=1,column=3)
                
            self.highscore_sub_var = BooleanVar(value=True)
            self.highscore_subtract = ttk.Checkbutton(self.highscore_page, variable=self.highscore_sub_var, width=13, command=self.search_highscores, text="Subtraction", style="green_bg.TCheckbutton")
            self.highscore_subtract.grid(row=2,column=3)
                
            self.highscore_mult_var = BooleanVar(value=True)
            self.highscore_multiply = ttk.Checkbutton(self.highscore_page, variable=self.highscore_mult_var, width=13, command=self.search_highscores, text="Multiplication", style="green_bg.TCheckbutton")
            self.highscore_multiply.grid(row=3,column=3)
                
            self.highscore_div_var = BooleanVar(value=True)
            self.highscore_divide = ttk.Checkbutton(self.highscore_page, variable=self.highscore_div_var, width=13, command=self.search_highscores, text="Division", style="green_bg.TCheckbutton")
            self.highscore_divide.grid(row=4,column=3)

            self.highscore_output_box=scrolledtext.ScrolledText(self.highscore_page,height=8,width=15,font="Arial 30 bold")
            self.highscore_output_box.grid(row=1, column=0, columnspan=3, rowspan=4)

            self.search_highscores()
        
    def next_question(self,event=None):  #Changes the question, writes the result, and clears the entry
        global question_number
        if self.answer_box.get() != "":     #Only proceeds if they've entered something
            user_answer_list.append(int(self.answer_box.get()))
            self.answer_box.delete(0, 'end')
            question_number += 1
            if question_number != len(correct_answer_list): #Show the next question
                question_var.set(problem_list[question_number])
            elif question_number == len(correct_answer_list):   #If they've reached the end unbind the enter key, and move to the resultsx
                window.unbind("<Return>")
                self.results()

    def search_highscores(self, val=None):  #Iterates through the highscore file and then writes all the matching ones to the file 
        difficulty = str(self.highscore_difficulty_value.get())
        x=[]
        if difficulty == "Difficulty": difficulty = "Medium"
        self.highscore_output_box.tag_config("centered", justify=CENTER)

        self.highscore_output_box.configure(state="normal")     #Resets everything to go again
        self.highscore_output_box.delete(1.0, 'end')
        current_highscore_list.clear()

        with open("Highscores.txt") as highscore_file:      #Opens the file
            for line in highscore_file:
                line = line.rstrip()
                line = line.split(",")
                if str(line[2]) == difficulty and str(line[3]) == str(self.highscore_add_var.get()) and str(line[4]) == str(self.highscore_sub_var.get()) and str(line[5]) == str(self.highscore_mult_var.get()) and str(line[6]) == str(self.highscore_div_var.get()):
                    x.clear()                   #Messy, but it combines the first 2 items into a list and puts that list onto another list, which is later displayed. 
                    x.append(line[0])           #Doing it this way allows me to sort the highscores with the names fixed
                    y = (str(line[1]) + "\n")
                    x.append(y)
                    current_highscore_list.append(x)
        current_highscore_list.sort(key= lambda x: x[0], reverse=True)    #Sorts the highscores
        for i in current_highscore_list:
            self.highscore_output_box.insert("end", i[1],"centered")       #Writes it to the output box

        self.highscore_output_box.configure(state="disabled")

            
def is_num(in_string,action_type):  #Checks that the user only enters numbers
    if action_type == '1': #insert
        if not in_string.isdigit():
            return False
    return True

def one_char(in_string, action_type):    #Checks the the user only enters one alphanumric character
    if action_type == '1': #insert
        if len(in_string) > 1:
            return False
        elif in_string.isalpha() or in_string.isdigit():
            return True
        else:
            return False
    return True

def calc_score():       #I made it a function so that I could change how I calculated the score easily. I was tossing it up between this method and another one.
    global score
    global duration
    return score/duration

def generate_problems(difficulty="Medium", add=True, sub=True, mult=True, div=True):        #Generates problems according to the formula laid out in Problem Difficulty Explanation.xlsx
    selected_functions=[]
    if difficulty == "Difficulty": difficulty = "Medium"
    selected_functions.clear()
    problem_list.clear()
    correct_answer_list.clear()
    if add: selected_functions.append("add")    #Only make questions for the operations the user selcted
    if sub: selected_functions.append("sub")
    if mult: selected_functions.append("mult")
    if div: selected_functions.append("div")
    for i in range(NUM_QUESTIONS):      #Used a constant so I can easily change the number of questions
        num_1 = 0
        num_2 = 0
        current_operation = (rnd.choice(selected_functions))
        if current_operation == "add":              #This is the best way I could figure out to do a matrix of results
            if difficulty == "Easy":                #I've detailed what the difficulties are in a more readable way in the explanatory document
                num_1 = rnd.randint(1,9)            #I'm not commenting it all because it's similar
                num_2 = rnd.randint(1,9)            #Depending on the difficulty it determines 1 or 2 numbers
            elif difficulty == "Medium":            #Then it combines them into a question as a string, and puts that on a list
                num_1 = rnd.randint(1,9)            #And writes the anwer to another list
                num_2 = rnd.randint(10,99)
            elif difficulty == "Hard":
                num_1 = rnd.randint(1,9) * int(rnd.choice([2,5,10]))
                num_2 = rnd.randint(10,99)
            elif difficulty == "Expert":
                num_1 = rnd.randint(10,99)
                num_2 = rnd.randint(10,99)
            full_problem = str(num_1) +  " + " + str(num_2)
            problem_list.append(full_problem)
            correct_answer_list.append(num_1+num_2)
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
                correct_answer_list.append(num_1-num_2)
            else:
                full_problem = str(num_2) +  " - " + str(num_1)
                correct_answer_list.append(num_2-num_1)
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
            correct_answer_list.append(num_1*num_2)
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
            correct_answer_list.append(int((num_1*num_2)/num_1))


            
window = Tk()

current_highscore_list=[]           #That's a lot of variables
highscore_list=[]                   #I probably could've used fewer variables, but that would've made the code longer and more convoluted
problem_list=[]
user_answer_list=[]
correct_answer_list=[]
answer = StringVar()
question_var = StringVar()
init_1 = StringVar()
init_2 = StringVar
init_3 = StringVar()
question_number = 0
start_time = 0
duration = 0
score = 0
NUM_QUESTIONS=100

window.geometry("500x500")
window.title("George's 100 Basic Facts")

#Putting it down here makes the code up there easier to read without a massive block of text or a line going way off to the right
instruction_text = "Welcome to George's 100 Basic Facts. \n On the main menu you can select what operations (addition, subtraction, multiplication, division) you want to practice, and what difficulty you want the questions to be. \n Once you're ready you can click start, and the first question will come up, and the timer will start. \n Put your answer in the box, and press enter to move to the next question. After 100 questions you can see your results, and save your resulta. \n The points are determined by the number of correct answers divided by how long it took. \n That's all you need to know, enjoy."

main_window()
