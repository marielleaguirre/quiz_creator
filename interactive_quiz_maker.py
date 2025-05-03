# Create a program that ask user for a question, it will also ask for 4 possible answer (a, b, c, d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

import os  # for file operations
from termcolor import colored  # for color formatting
import time  # for adding delays

# ask the user to enter the file name where quiz questions will be saved
quiz_file = input(colored("Enter the quiz file name (e.g., 'quiz_data.txt'): ", "blue")).strip()

# function to save the quiz question data to file
def save_to_file(question_data): 
    with open(quiz_file, "a", encoding="utf-8") as file:
        file.write("\n" + "-" * 50 + "\n")
        file.write("Question:\n" + question_data['question'] + "\n")
        for label, choice in question_data['choices'].items():
            file.write(f" {label}) {choice}\n")
        file.write("Answer:\n" + question_data['answer'] + "\n")
        file.write("-" * 50 + "\n")
        

# function to create the quiz by asking for user input
def create_quiz(): 
    # display a welcoming message
    print(colored("\nWelcome to my Python Quiz Creator! *ฅ^•ﻌ•^ฅ*\n", "yellow", attrs=["bold"]))
    time.sleep(1)

    print(colored("Let's get started! Add as many questions as you want ₍^. .^₎⟆", "green"))

    # start a loop that allows the user to add multiple questions
    while True: 
        # ask the user to input a question
        question = input(colored("Enter your question: ", "blue")).strip()
    
        # ask the user to provide 4 possible choices (a, b, c, d)
        choices = {}
        for option in ['a', 'b', 'c', 'd']:
            choice = input(colored(f" ⋆˚✿˖° Enter choice {option.upper()}: ", "cyan")).strip()
            choices[option] = choice
        
        # ask the user to input the correct answer
        correct = input(colored("Enter the correct answer (a, b, c, or d): ", "green")).strip().lower()

        # validate the correct answer
        if correct not in choices: 
            print(colored("Invalid answer (╥﹏╥). Must be one of: a, b, c, d.\n", "red"))
            continue

        # create a dictionary to hold the question data
        question_data = {
            "question": question,
            "choices": choices,
            "answer": correct
        }

        # save the question and answers to the specified quiz file
        save_to_file(question_data)
        print(colored("Question saved successfully! /ᐠ. .ᐟ\ Ⳋ ✧\n", "yellow"))  

        # ask the user if they want to add another question
        again = input(colored("Add another question? (๑•᎑•๑) (type 'yes' to continue and 'no' to exit): ", "blue"))
        if again != 'yes':
            print(colored("\nCongratulations on creating your quiz!", "magenta", attrs=["bold"]))
            print(colored("Exiting... Goodbye! (∩˃ω˂∩)", "red", attrs=["bold"]))
            time.sleep(1)
            break
        
    print(colored(f"\nAll questions saved to '{quiz_file}'.", "green"))  # diplay a message confirming that all questions have been saved to the specified file

# function to check file doesn't exists and create it if necessary
def main_file(): 
    # check if the quiz file already exists. if not, create a file with introductory header
    if not os.path.exists(quiz_file):
        with open(quiz_file, "w") as f:
            f.write("=== Quiz Questions ===\n\n")

    create_quiz()

if __name__ == "__main__":
    main_file()