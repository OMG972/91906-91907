import json

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


run_quiz_easy()