import json
import tkinter as tk
from tkinter import *

def quit():
    root.destroy()

def run_quiz_easy():
    with open("assesment-quiz-easy.json", "r") as file:
        quiz_data = json.load(file)
    
    global score
    score = 0

    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        print (f"Your score is {score}")

    if score >= 3:
        print("Congrats you passed!")
        print("Onto the next level")
        run_quiz_medium()
    elif score < 3:
        print("Better luck next time")


def run_quiz_medium():
    with open("assesment-quiz-medium.json", "r") as file:
        quiz_data = json.load(file)

        global score

    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        print (f"Your score is {score}")

    if score >= 6:
        print("Congrats you passed!")
        print("Onto the next level")
        run_quiz_hard()
    elif score < 6:
        print("Better luck next time")


def run_quiz_hard():
    with open("assesment-quiz-hard.json", "r") as file:
        quiz_data = json.load(file)

        global score

    for question_id, content in quiz_data.items():
        print(f"\n{content['question']}")
        
        for choice in content['choices']:
            print(f"- {choice}")
        
        answer = input("Enter answer: ").strip()

        if answer.lower() == content['answer'].lower():
            print("Correct")
            score += 1
        else:
            print(f"Incorrect, the right answer is {content['answer']}")
        
        print (f"Your score is {score}")
        
    if score >= 9:
        print("Congrats you passed!")
        print("You beat all the levels!")
        run_quiz_medium()
    elif score < 9:
        print("Better luck next time")


root = tk.Tk()
root.title("Quiz")
root.geometry("500x500")
root.resizable(0,0)
root.configure(bg="lightblue")


lbl1 = Label(root, text="Knowledge quiz", font="Arial 22 bold", fg="Black").place(x=140, y=0)

lbl2 = Label(root, text=f"Welcome to the knowledge quiz! This quiz is designed \n as a quick fun way to test your knowledge", font="Arial 14 bold", fg="Black"). place(x=0, y=40)

button_run_quiz = Button(root, text = "Begin quiz", width = 10, command = run_quiz_easy)
button_run_quiz.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()