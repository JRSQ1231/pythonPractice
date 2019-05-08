from sys import argv
# list the variables
script, filename = argv
# this line names txt as a variable and sets it to open() a file.
txt = open(filename)
# the next lines print out some text and then opens the file entered when the program was called.
print(f"Here's your file {filename}:")
print(txt.read())
# more text, the the program asks for user input to define the file_again variable
print("Type the filename again:")
file_again = input("> ")
# this line runs the open module
txt_again = open(file_again)
# this line prints the entire file opened in the previous line.
print(txt_again.read())