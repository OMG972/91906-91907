import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Quiz")
root.geometry("503x300")
root.resizable(0,0)
root.configure(bg="lightblue")

class settings:
    #Automaticly sets dark_mode and coulourblind_mode to off
    dark_mode=False
    colourblind_mod=False
    
    def quit():
        if messagebox.askokcancel(title=None, message="Are you sure you want to quit?"):
            root.destroy()
            #Closes the window

    def darkmode():
        #Running darkmode turns it on and turns off colourblind mode.
        settings.darkmode=True
        settings.colourblind_mode=False

        root.configure(bg="#413839")

        settings.update_all_windows()

    def colourblind_mode():
        #Running colourblind mode turns it on and turns off darkmode.
        settings.darkmode=False
        settings.colourblind_mode=True

        root.configure(bg="#0072B2")

        settings.update_all_windows()

    def update_all_windows():
        #Changes the colour of all open windows
        settings.update_widgets(root)

        for window in root.winfo_children():
            if isinstance(window, Toplevel):
                settings.update_widgets(window)

    def update_widgets(window):
        #Runs the code to change the colours checks if darkmode or colourblind mode is turned on and changes the colours if it is
        for widget in window.winfo_children():
            if settings.darkmode:
                try:
                    widget.configure(bg="#413839", fg="white")
                except:
                    pass
            
            elif settings.colourblind_mode:
                try:
                    widget.configure(bg="#0072B2", fg="black")
                except:
                    pass
            
            if widget.winfo_children():
                settings.update_widgets(widget)

class run_quiz:
    def next_question(question_label, quiz_state, user_entry, option1, option2, option3, option4, button_next, result):

        #Gets the user entry and the question
        current = quiz_state["questions"][quiz_state["question_index"]]
        answer=user_entry.get().strip()

        #Tests to see if the answer is correct or not and if it is adds one to the score
        if answer.strip().lower() == current["answer"].lower().strip():
            quiz_state["score"] += 1
            result.configure(text=f"Correct")

        else:
            result.configure(text=f"Incorrect")

        #Resets the user entry box to blank
        user_entry.delete(0, END)

        #Moves to next question
        quiz_state["question_index"]+=1

        #Prints out all the choices
        if quiz_state["question_index"]<len(quiz_state["questions"]):
            current=quiz_state["questions"][quiz_state["question_index"]]
            question_label.config(text=current["question"])

            option1.configure(text=current["choices"][0])
            option2.configure(text=current["choices"][1])
            option3.configure(text=current["choices"][2])
            option4.configure(text=current["choices"][3])

        else:
            score = quiz_state["score"]

            #Shows the results of the quiz
            question_label.configure(text=f"Quiz complete! Your score is {score}/4")

            option1.config(text="")
            option2.config(text="")
            option3.config(text="")
            option4.config(text="")

            #Disables the next button once quiz is finished
            button_next.config(state=DISABLED)

            #Tells if you passed the quiz or not
            if quiz_state["level"]=="easy" and score >=3:
                result.configure(text=f"You passed")

            elif quiz_state["level"]=="medium" and score >=3:
                result.configure(text=f"You passed")

            elif quiz_state["level"]=="hard" and score >=3:
                result.configure(text=f"You passed")

            else:
                result.configure(text=f"You didnt pass ):")


    def run_quiz_easy(question_label, quiz_state, option1, option2, option3, option4):
        #Runs easy level quiz
        file_path=r"N:\13PRG-LIA\st22388 Sharn\Assessment\91906 Sharn_Muir\assesment-quiz-easy.json"

        with open(file_path, "r") as file:
            quiz_data=json.load(file)
    
        #Sets variables
        quiz_state["score"]=0
        quiz_state["question_index"]=0
        quiz_state["questions"]=list(quiz_data.values())
        quiz_state["level"]="easy"

        question_label.config(text=quiz_state["questions"][0]["question"])

        option1.config(text=quiz_state["questions"][0]["choices"][0])
        option2.config(text=quiz_state["questions"][0]["choices"][1])   
        option3.config(text=quiz_state["questions"][0]["choices"][2])   
        option4.config(text=quiz_state["questions"][0]["choices"][3])     

    def run_quiz_medium(question_label, quiz_state, option1, option2, option3, option4):
        #Runs medium level quiz
        file_path=r"N:\13PRG-LIA\st22388 Sharn\Assessment\91906 Sharn_Muir\assesment-quiz-medium.json"

        with open(file_path, "r") as file:
            quiz_data=json.load(file)
    
        #Sets variables
        quiz_state["score"]=0
        quiz_state["question_index"]=0
        quiz_state["questions"]=list(quiz_data.values())
        quiz_state["level"]="medium"

        question_label.config(text=quiz_state["questions"][0]["question"])

        option1.config(text=quiz_state["questions"][0]["choices"][0])
        option2.config(text=quiz_state["questions"][0]["choices"][1])   
        option3.config(text=quiz_state["questions"][0]["choices"][2])   
        option4.config(text=quiz_state["questions"][0]["choices"][3])  


    def run_quiz_hard(question_label, quiz_state, option1, option2, option3, option4):
        #Runs hard level quiz
        file_path=r"N:\13PRG-LIA\st22388 Sharn\Assessment\91906 Sharn_Muir\assesment-quiz-hard.json"

        with open(file_path, "r") as file:
            quiz_data=json.load(file)
    
        #Sets variables
        quiz_state["score"]=0
        quiz_state["question_index"]=0
        quiz_state["questions"]=list(quiz_data.values())
        quiz_state["level"]="hard"

        question_label.config(text=quiz_state["questions"][0]["question"])

        option1.config(text=quiz_state["questions"][0]["choices"][0])
        option2.config(text=quiz_state["questions"][0]["choices"][1])   
        option3.config(text=quiz_state["questions"][0]["choices"][2])   
        option4.config(text=quiz_state["questions"][0]["choices"][3])  

class guis:
    
    def easy_gui(run_quiz_easy, next_question, settings_gui):
        easy = Toplevel(root)
        easy.geometry("325x470")
        easy.title("Easy quiz")
        easy.resizable(FALSE,FALSE)
        easy.configure(bg="Lightgreen")
    
        #Displays the title
        easy_lbl1 = Label(easy, text="Easy quiz", font="Arial 22 bold", fg="Black", bg = "Lightgreen")
        easy_lbl1.grid(row=1, column=0, columnspan=2, pady=(15,10))

        #Displays the question
        question = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
        question.grid(row=2, column=0, columnspan=3, pady=10)

        #Dispplays the options
        option1 = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
        option1.grid(row=3, column=0, sticky="w", pady=5, padx=10)

        option2 = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
        option2.grid(row=4, column=0, sticky="w", pady=5, padx=10)

        option3 = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
        option3.grid(row=5, column=0, sticky="w", pady=5, padx=10)

        option4 = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
        option4.grid(row=6, column=0, sticky="w", pady=5, padx=10)

        quiz_state = {}

        run_quiz_easy(question, quiz_state, option1, option2, option3, option4)

        #Lets user input their answer
        user_entry = Entry(easy, justify=LEFT, font="Arial 22 bold")
        user_entry.grid(row=7, column=0, columnspan=2, pady=20)

        #Displays the result
        result = Label(easy, text="", font="Arial 14 bold", fg="Black", bg="Lightgreen")
        result.grid(row=8, column=0, columnspan=2, pady=20)

        #Button to enter answer
        button_next = Button(easy, text = "Next", width = 10, bg = "Lightgreen", command = lambda: next_question(question, quiz_state, user_entry, option1, option2, option3, option4, button_next, result))
        button_next.grid(row = 9, column = 0, sticky="w", padx = 10, pady = 10)

        #Button to run settings
        button_settings = Button(easy, text = "Settings", width = 10, bg = "Lightgreen", command = settings_gui)
        button_settings.grid(row=9, column=0, columnspan= 2, pady = 10)

        #Button to quit the quiz
        button_quit = Button(easy, text = "Quit", width = 10, bg = "Lightgreen", command = settings.quit)
        button_quit.grid(row=9, column=1, pady = 10)


    def medium_gui(run_quiz_medium, next_question, settings_gui):
        medium = Toplevel(root)
        medium.geometry("325x470")
        medium.title("Medium quiz")
        medium.resizable(FALSE,FALSE)
        medium.configure(bg="Yellow")
    
        #Displays the title
        lbl1 = Label(medium, text="Medium quiz", font="Arial 22 bold", fg="Black", bg = "Yellow")
        lbl1.grid(row=1, column=0, columnspan=2, pady=(15,10))

        #Displays the question
        question = Label(medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
        question.grid(row=2, column=0, columnspan=3, pady=10)

        #Dispplays the options
        option1 = Label(medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
        option1.grid(row=3, column=0, sticky="w", pady=5, padx=10)

        option2 = Label(medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
        option2.grid(row=4, column=0, sticky="w", pady=5, padx=10)

        option3 = Label(medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
        option3.grid(row=5, column=0, sticky="w", pady=5, padx=10)

        option4 = Label(medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
        option4.grid(row=6, column=0, sticky="w", pady=5, padx=10)

        quiz_state = {}

        run_quiz_medium(question, quiz_state, option1, option2, option3, option4)

        #Lets user input their answer
        user_entry = Entry(medium, justify=LEFT, font="Arial 22 bold")
        user_entry.grid(row=7, column=0, columnspan=2, pady=20)

        #Displays the result
        result = Label(medium, text="", font="Arial 14 bold", fg="Black", bg="Yellow")
        result.grid(row=8, column=0, columnspan=2, pady=20)

        #Button to enter answer
        button_next = Button(medium, text = "Next", width = 10, bg = "Yellow", command = lambda: next_question(question, quiz_state, user_entry, option1, option2, option3, option4, button_next, result))
        button_next.grid(row = 9, column = 0, sticky="w", padx = 10, pady = 10)

        #Button to run settings
        button_settings = Button(medium, text = "Settings", width = 10, bg = "Yellow", command = settings_gui)
        button_settings.grid(row=9, column=0, columnspan= 2, pady = 10)

        #Button to quit the quiz
        button_quit = Button(medium, text = "Quit", width = 10, bg = "Yellow", command = settings.quit)
        button_quit.grid(row=9, column=1, pady = 10)

    def hard_gui(run_quiz_hard, next_question, settings_gui):
        hard = Toplevel(root)
        hard.geometry("325x470")
        hard.title("Hard quiz")
        hard.resizable(FALSE,FALSE)
        hard.configure(bg="orange")
    
        #Displays the title
        lbl1 = Label(hard, text="Hard quiz", font="Arial 22 bold", fg="Black", bg = "Orange")
        lbl1.grid(row=1, column=0, columnspan=2, pady=(15,10))

        #Displays the question
        question = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
        question.grid(row=2, column=0, columnspan=3, pady=10)

        #Dispplays the options
        option1 = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
        option1.grid(row=3, column=0, sticky="w", pady=5, padx=10)

        option2 = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
        option2.grid(row=4, column=0, sticky="w", pady=5, padx=10)

        option3 = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
        option3.grid(row=5, column=0, sticky="w", pady=5, padx=10)

        option4 = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
        option4.grid(row=6, column=0, sticky="w", pady=5, padx=10)

        quiz_state = {}

        run_quiz_hard(question, quiz_state, option1, option2, option3, option4)

        #Lets user input their answer
        user_entry = Entry(hard, justify=LEFT, font="Arial 22 bold")
        user_entry.grid(row=7, column=0, columnspan=2, pady=20)

        #Displays the result
        result = Label(hard, text="", font="Arial 14 bold", fg="Black", bg="Orange")
        result.grid(row=8, column=0, columnspan=2, pady=20)

        #Button to enter answer
        button_next = Button(hard, text = "Next", width = 10, bg = "Orange", command = lambda: next_question(question, quiz_state, user_entry, option1, option2, option3, option4, button_next, result))
        button_next.grid(row = 9, column = 0, sticky="w", padx = 10, pady = 10)

        #Button to run settings
        button_settings = Button(hard, text = "Settings", width = 10, bg = "Orange", command = settings_gui)
        button_settings.grid(row=9, column=0, columnspan= 2, pady = 10)

        #Button to quit the quiz
        button_quit = Button(hard, text = "Quit", width = 10, bg = "Orange", command = settings.quit)
        button_quit.grid(row=9, column=1, pady = 10)

    def settings_gui():
        settings_window = Toplevel(root)
        settings_window.geometry("320x330")
        settings_window.title("Settings")
        settings_window.resizable(0,0)
        settings_window.configure(bg="Lightgrey")

        #Title
        lbl1 = Label(settings_window, text="Settings", font="Arial 22 bold", fg="Black", bg = "Lightgrey")
        lbl1.grid(row=0, column=1, pady=5, padx=10)

        #Button to implement darkmode
        button_darkmode = Button(settings_window, text = "Dark mode", width = 10, bg = "Lightgrey", command = settings.darkmode)
        button_darkmode.grid(row=1, column=0, ipady = 10, padx = 5, pady = 10)

         #Button to implement coulourblind mode
        button_colourblind_mode = Button(settings_window, text = "Colour blind mode", width = 14, bg = "Lightgrey", command = settings.colourblind_mode)
        button_colourblind_mode.grid(row=1, column=1, ipady = 10, padx = 5, pady = 10)

        #Button to quit
        button_quit = Button(settings_window, text = "Quit", width = 10, bg = "Lightgrey", command = settings.quit)
        button_quit.grid(row=1, column=2, ipady = 10, padx = 5, pady = 10)

    def main_gui(easy_gui, medium_gui, hard_gui, settings_gui, run_quiz_easy, run_quiz_medium, run_quiz_hard, next_question):
        #Title
        lbl1 = Label(root, text="Knowledge quiz", font="Arial 22 bold", fg="Black", bg = "Lightblue").place(x=140, y=0)

        #Brief introduction to the quiz
        lbl2 = Label(root, text=f"Welcome to the knowledge quiz! This quiz is designed \n as a quick fun way to test your knowledge", font="Arial 14 bold", fg="Black", bg = "Lightblue"). place(x=0, y=40)

        #Button to run the quiz
        button_run_quiz = Button(root, text = "Begin quiz easy", width = 14, bg = "lightblue", command = lambda: easy_gui(run_quiz_easy, next_question, settings_gui))
        button_run_quiz.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

        #Button to run medium level quiz
        button_run_quiz_medium = Button(root, text = "Begin quiz medium", width = 14, bg = "lightblue", command = lambda: medium_gui(run_quiz_medium, next_question, settings_gui))
        button_run_quiz_medium.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

        #Button to run hard level quiz
        button_run_quiz_hard = Button(root, text = "Begin quiz hard", width = 14, bg = "lightblue", command = lambda: hard_gui(run_quiz_hard, next_question, settings_gui))
        button_run_quiz_hard.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

        #Button to run settings
        button_settings = Button(root, text = "Settings", width = 7, bg = "lightblue", command = lambda: settings_gui())
        button_settings.pack(side = LEFT, ipady =10, padx = 5, pady = 10)

        #Button to quit the quiz
        button_quit = Button(root, text = "Quit", width = 10, bg = "lightblue", command = quit)
        button_quit.pack(side = RIGHT, ipady = 10, padx = 10, pady = 10)

def main():
    guis.main_gui(guis.easy_gui, guis.medium_gui, guis.hard_gui, guis.settings_gui, run_quiz.run_quiz_easy, run_quiz.run_quiz_medium, run_quiz.run_quiz_hard, run_quiz.next_question)
    
    root.mainloop()
    
if __name__ =="__main__":
    main()