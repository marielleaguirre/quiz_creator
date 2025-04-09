# Create a program that ask user for a question, it will also ask for 4 possible answer (a, b, c, d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# ask the user to enter the file name where quiz questions will be saved
# check if the quiz file already exists. if not, create a file with introductory header
# display a welcoming message
# start a loop that allows the user to add multiple questions
#   ask the user to input a question
#   ask the user to provide 4 possible choices (a, b, c, d)
#   ask the user to input the correct answer
#   validate the correct answer
#       if the correct answer matches one of the possible choices, continue
#       else, print "invalid" and prompt the user to enter the question again
#   save the question and answers to the specified quiz file
#   after saving a question, ask the user if they want to add another question
#       if the answer is not "yes", exit the loop and diplay a goodbye message
#       diplay a message confirming that all questions have been saved to the specified file

# function to save the quiz question data to file
def save_to_file(question_data): 

# function to create the quiz by asking for user input
def create_quiz(): 

# function to check file doesn't exists and create it if necessary
def main_file(): 