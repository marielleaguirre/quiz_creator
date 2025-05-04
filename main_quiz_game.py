# Create a Quiz program that read the output file of the Quiz Creator
# The user will answer the randomely selected question and check if the answer is correct

# import necessary libraries for file handling, randomization, and GUI creation
import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

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
def start_quiz(quiz_data):
    # initialize the quiz state: current index, score, total number of questions, etc.
    current = {"index": -1, "score": 0, "total": len(quiz_data), "data": quiz_data, "current_question": None}

    # function to load the next question
    def load_next_question():
        if not current["data"]:  # if no more questions, end the quiz
            return end_quiz()
        
        # select a random question, remove it from the data pool
        current["current_question"] = random.choice(current["data"])
        current["data"].remove(current["current_question"])

        # display the question and choices on the user interface
        question_label.config(text=current["current_question"]["questions"])
        for key in ['a', 'b', 'c', 'd']:
            choice = current["current_question"]["choices"][key]
            buttons[key].config(text=f"{key.upper()}) {choice}", state="normal")  # enable answer buttons

        feedback_label.config(text="")  # reset feedback label
        next_button.config(state="disabled")  # disable next button until answer is chosen

    # function to check if the selected answer is correct
    def check_answer(selected):
        correct = current["current_question"]["answer"]  # get the correct answer
        if selected == correct:  # if correct, update score and display "Correct" feedback
            feedback_label.config(text="Correct!")
            current["score"] += 1
        else:  # if incorrect, show the correct answer
                correct_text = current["current_question"]["choices"][correct]
                feedback_label.config(text=f"Wrong! Correct answer is {correct.upper()}) {correct_text}")

        # disable answer buttons after selection an answer
        for button in buttons.values():
            button.config(state="disabled")
        next_button.config(state="normal")  # enable next question button

    # function to end the quiz and display the final score
    def end_quiz():
        for widget in root.winfo_children():  # remove all widgets to clean the window
            widget.destroy()

        # display the final score
        result = f" Quiz Finished! Your Score: {current['score']}/{current['total']}"
        result_label = tk.Label(root, text=result)
        result_label.pack(pady=20)

        # display a motivational message based on the score
        if current["score"] == current["total"]:
            message = "Perfect score! You're a quiz master!"
        elif current["score"] >= current["total"] // 2:
            message = "Nice try! You did well!"
        else:
            message = "Don't worry! Try again and do better next time!"

        # diplay the result message in a pop up
        messagebox.showinfo("Quiz Result", message)

    # configure the root window (dark themed)
    root.configure(bg="#222")

    # style configuration for buttons
    style = ttk.Style()
    style.configure("TButton")

    # label to display the question
    question_label = tk.Label(root, text="")
    question_label.pack(pady=20)

    # create answer buttons for choice a, b, c, d
    buttons = {}
    for key in ['a', 'b', 'c', 'd']:
        buttons[key] = tk.Button(root, text="", command=lambda k=key: check_answer(k))
        buttons[key].pack(pady=5)

    # feedback label to show whether the answer is correct or not
    feedback_label = tk.Label(root, text="")
    feedback_label.pack(pady=10)

    # button to move to the next question
    next_button = tk.Button(root, text="Next Question ⭢", command=load_next_question)
    next_button.pack(pady=10)

    # load the first question
    load_next_question()
    
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
    root.deiconify()
    start_quiz(questions)
    root.mainloop()  # run the tkinter event loop

# execute the main function if the script is run directly
if __name__ == "__main__":
    main_program()