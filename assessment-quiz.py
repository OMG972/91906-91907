import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def quit():
    #Closes the window
    root.destroy()

def settings():
    ""

def run_quiz_easy():
    #Runs easy level quiz
    with open("assesment-quiz-easy.json", "r") as file:
        quiz_data = json.load(file)
    
    #Sets a global variable score to keep score of how many questions you got right
    global score
    score = 0

    #Prints questions
    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        #Takes in users answer
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        #Prints score
        print (f"Your score is {score}")

    #Checks if you passed the level
    if score >= 3:
        print("Congrats you passed!")
        print("Onto the next level")
        run_quiz_medium()
    elif score < 3:
        print("Better luck next time")


def run_quiz_medium():
    #Runs medium level quiz
    with open("assesment-quiz-medium.json", "r") as file:
        quiz_data = json.load(file)

        global score

    #Prints questions
    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        #Takes in users answer
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        #Print score
        print (f"Your score is {score}")

    #Checks if you passed the level
    if score >= 6:
        print("Congrats you passed!")
        print("Onto the next level")
        run_quiz_hard()
    elif score < 6:
        print("Better luck next time")


def run_quiz_hard():
    #Runs hard level quiz
    with open("assesment-quiz-hard.json", "r") as file:
        quiz_data = json.load(file)

        global score

    #Prints questions
    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        #Takes in users answer
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        #Prints score
        print (f"Your score is {score}")
        
    #Checks if you passed the level
    if score >= 9:
        print("Congrats you passed!")
        print("You beat all the levels!")
        run_quiz_medium()
    elif score < 9:
        print("Better luck next time")


root = tk.Tk()
root.title("Quiz")
root.geometry("503x300")
root.resizable(0,0)
root.configure(bg="lightblue")


def easy_gui():
    easy = Toplevel(root)
    easy.geometry("320x300")
    easy.title("Easy quiz")
    easy.resizable(0,0)
    easy.configure(bg="Lightgreen")
    
    lbl1 = Label(easy, text="Easy quiz", font="Arial 22 bold", fg="Black", bg = "Lightgreen")
    lbl1.grid(row=0, column=0, pady=5, padx=10)

    question = Label(easy, text="", font="Arial 14 bold", fg="Black", bg = "Lightgreen")
    question.grid(row=1, column=0, ipady=10)

    box1 = Entry(easy, justify=LEFT, font="Arial 22 bold")
    box1.grid(row=2, column=0)

    #Button to run settings
    button_settings = Button(easy, text = "Settings", width = 10, bg = "Lightgreen", command = "")
    button_settings.grid(row=3, column=0, ipady =10, padx = 5, pady = 10)

    #Button to quit the quiz
    button_quit = Button(easy, text = "Quit", width = 10, bg = "Lightgreen", command = quit)
    button_quit.grid(row=4, column=0, ipady = 10, padx = 5, pady = 10)


def medium_gui():
    Medium = Toplevel(root)
    Medium.geometry("320x300")
    Medium.title("Medium quiz")
    Medium.resizable(0,0)
    Medium.configure(bg="Yellow")
    
    lbl1 = Label(Medium, text="Medium quiz", font="Arial 22 bold", fg="Black", bg = "Yellow")
    lbl1.grid(row=0, column=0, pady=5, padx=10)

    question = Label(Medium, text="", font="Arial 14 bold", fg="Black", bg = "Yellow")
    question.grid(row=1, column=0, ipady=10)

    box1 = Entry(Medium, justify=LEFT, font="Arial 22 bold")
    box1.grid(row=2, column=0)

    #Button to run settings
    button_settings = Button(Medium, text = "Settings", width = 10, bg = "Yellow", command = "")
    button_settings.grid(row=3, column=0, ipady =10, padx = 5, pady = 10)

    #Button to quit the quiz
    button_quit = Button(Medium, text = "Quit", width = 10, bg = "Yellow", command = quit)
    button_quit.grid(row=4, column=0, ipady = 10, padx = 5, pady = 10)


def hard_gui():
    hard = Toplevel(root)
    hard.geometry("320x300")
    hard.title("Hard quiz")
    hard.resizable(0,0)
    hard.configure(bg="Orange")
    
    lbl1 = Label(hard, text="Hard quiz", font="Arial 22 bold", fg="Black", bg = "Orange")
    lbl1.grid(row=0, column=0, pady=5, padx=10)

    question = Label(hard, text="", font="Arial 14 bold", fg="Black", bg = "Orange")
    question.grid(row=1, column=0, ipady=10)

    box1 = Entry(hard, justify=LEFT, font="Arial 22 bold")
    box1.grid(row=2, column=0)

    #Button to run settings
    button_settings = Button(hard, text = "Settings", width = 10, bg = "Orange", command = "")
    button_settings.grid(row=3, column=0, ipady =10, padx = 5, pady = 10)

    #Button to quit the quiz
    button_quit = Button(hard, text = "Quit", width = 10, bg = "Orange", command = quit)
    button_quit.grid(row=4, column=0, ipady = 10, padx = 5, pady = 10)


#Title
lbl1 = Label(root, text="Knowledge quiz", font="Arial 22 bold", fg="Black", bg = "lightblue").place(x=140, y=0)

#Brief introduction to the quiz
lbl2 = Label(root, text=f"Welcome to the knowledge quiz! This quiz is designed \n as a quick fun way to test your knowledge", font="Arial 14 bold", fg="Black", bg = "lightblue"). place(x=0, y=40)

#Button to run the quiz
button_run_quiz = Button(root, text = "Begin quiz easy", width = 14, bg = "lightblue", command = easy_gui)
button_run_quiz.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

#Button to run meduim level quiz
button_run_quiz_medium = Button(root, text = "Begin quiz meduim", width = 14, bg = "lightblue", command = medium_gui)
button_run_quiz_medium.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

#Button to run hard level quiz
button_run_quiz_hard = Button(root, text = "Begin quiz hard", width = 14, bg = "lightblue", command = hard_gui)
button_run_quiz_hard.pack(side = LEFT, ipady = 10, padx = 5, pady = 10)

#Button to run settings
button_settings = Button(root, text = "Settings", width = 7, bg = "lightblue", command = "")
button_settings.pack(side = LEFT, ipady =10, padx = 5, pady = 10)

#Button to quit the quiz
button_quit = Button(root, text = "Quit", width = 10, bg = "lightblue", command = quit)
button_quit.pack(side = RIGHT, ipady = 10, padx = 10, pady = 10)

root.mainloop()