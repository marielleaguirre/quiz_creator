# Create a program that ask user for a question, it will also ask for 4 possible answer (a, b, c, d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

import os # for file operations

# ask the user to enter the file name where quiz questions will be saved
quiz_file = input("Enter the quiz file name (e.g., 'quiz_data.txt'): ").strip()

# function to save the quiz question data to file
def save_to_file(question_data): 
    with open(quiz_file, "a", encoding="utf-8") as file:
        file.write("Question:\n" + question_data['question'] + "\n")
    for label, choice in question_data['choices'].items():
        file.write(f" {label}) {choice}\n")
    file.write("Answer:\n" + question_data['answer'] + "\n")
    file.write("-" * 50 + "\n")
        

# function to create the quiz by asking for user input
def create_quiz(): 
    # display a welcoming message
    print("\nWelcome to my Python Quiz Creator!")
    print("Let's get started! Add as many questions as you want :)")
    # start a loop that allows the user to add multiple questions
    while True: 
    #   ask the user to input a question
        question = input("Enter your question: ")
    
    #   ask the user to provide 4 possible choices (a, b, c, d)
        choices = {}
        for option in ['a', 'b', 'c', 'd']:
            choice = input(f"Enter choice {option.upper()}: ").strip()
            choices[option] = choice
        
    #   ask the user to input the correct answer
        correct = input("Enter the correct answer (a, b, c, or d): ").strip().lower()

    #   validate the correct answer
    #       if the correct answer matches one of the possible choices, continue
        if correct not in choices: # else, print "invalid" and prompt the user to enter the question again
            print("Invalid answer. Must be one of: a, b, c, d.")
            continue

    #   create a dictionary to hold the question data
        question_data = {
            "question": question,
            "choices": choices,
            "answer": correct
        }

    #   save the question and answers to the specified quiz file
        save_to_file(question_data)
        print("Question saved successfully!")  # diplay a message confirming that all questions have been saved to the specified file

    #   after saving a question, ask the user if they want to add another question
    #       if the answer is not "yes", exit the loop and diplay a goodbye message
    

# function to check file doesn't exists and create it if necessary
def main_file(): 
    # check if the quiz file already exists. if not, create a file with introductory header
    if not os.path.exists(quiz_file):
        with open(quiz_file, "w") as f:
            f.write("=== Quiz Questions ===\n\n")
