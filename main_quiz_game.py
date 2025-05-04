# Create a Quiz program that read the output file of the Quiz Creator
# The user will answer the randomely selected question and check if the answer is correct

# import necessary libraries for file handling, randomization, and GUI creation
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# function to load questions from the quiz file
def load_questions(filename):
    # check if the file exists, if not, return an empty list
    if not os.path.exists(filename):
        print("Quiz file not found.")
        return []
    
    # open the file and read its content
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().strip()  # strip any leading/trailing whitespace

    # split the content into individual questions by a separator (50 dashes)
    raw_questions = content.split("-" * 50)
    questions = []  # initialize an empty list to store the parsed questions

    # loop through each raw question
    for raw_content in raw_questions:
        # skip invalid or empty questions
        lines = [line.strip() for line in raw_content.strip().splitlines()]
        if not lines or "Question:" not in lines[0]:  # skip invalid or empty questions
            continue

        try:
            # extract the question text and choices (a, b, c, d)
            question_text = lines[1]
            choices = {
                'a': lines[2].split(")", 1)[1].strip(),  # split choice from the number and text
                'b': lines[3].split(")", 1)[1].strip(),
                'c': lines[4].split(")", 1)[1].strip(),
                'd': lines[5].split(")", 1)[1].strip()
            }
            # extract the correct answer (lowercased for comparison)
            answer = lines[7].strip().lower()

            # append the parsed question, choices, and answer to the questions list
            questions.append({
                "questions": question_text,
                "choices": choices,
                "answer": answer
            })
        except (IndexError, ValueError):  # skip if there's an error in parsing
            continue

    return questions  # return the list of parsed questions
    
# function to start the quiz
def start_quiz():

    # function to load the next question
    def load_next_question():
        # if no more questions, end the quiz
        # select a random question, remove it from the data pool
        # display the question and choices on the user interface
            # enable answer buttons
            # reset feedback label
            # disable next button until answer is chosen

    # function to check if the selected answer is correct
    def check_answer():
        # get the correct answer
        # if correct, update score and display "Correct" feedback
        # if incorrect, show the correct answer
        # disable answer buttons after selection an answer
        # enable next question button

    # function to end the quiz and display the final score
    def end_quiz():
        # remove all widgets to clean the window
        # display the final score
        # display a motivational message based on the score
        # diplay the result message in a pop up
    # configure the root window (dark themed)
    # style configuration for buttons
    # label to display the question
    # create answer buttons for choice a, b, c, d
    # feedback label to show whether the answer is correct or not
    # button to move to the next question
    # load the first question
    
# function to run the quiz game
def main_program():
    global root
    root = tk.Tk()  # create the main tkinter window
    root.title("My Quiz Game!")  # set the title of the window
    root.geometry("600x500")  # set the window size
    root.withdraw()  # hide the window initially 

    # prompt the user to select a quiz file
    file_path = filedialog.askopenfilename(title="Select Quiz File", filetypes=[("Text Files", "*.txt")])
    
    # if no file is selected, display an error message and exit
    if not file_path:
        messagebox.showerror("No file selected", "You must select a quiz file to proceed")
        return
    
    # load questions from the selected quiz file
    questions = load_questions(file_path)
    if not questions:
        messagebox.showerror("No Questions Found", "The selected file does not contain valid quiz questions.")
        return

    # show the main window and start the quiz
        # run the tkinter event loop

# execute the main function if the script is run directly
if __name__ == "__main__":
    main_program()