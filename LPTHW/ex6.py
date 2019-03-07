#  Assign 10 to types_of_people
types_of_people = 10
#  Assign the f-string to 'x' (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

#  Assign the word to binary.
binary = "binary"
#  Another assignment
do_not = "don't"
#  Assigning the f-string to 'y' (insert binary and do_not)
y = f"Those who know {binary} and those who {do_not}."

#  Print x
print(x)
#  Print y
print(y)

#  Print the string
print(f"I said: {x}")
#  Print the string
print(f"I also said: '{y}'")

#  Assign the boolean 'False' to hilarious
hilarious = False
#  Assign the string to joke_evalution
joke_evaluation = "Isn't that joke so funny?! {}"

#  Print the joke_evalutation statement and pass the hilarious variable.
print(joke_evaluation.format(hilarious))

#  Assign the string to w
w = "This is the left side of..."
#  Assign the string to e
e = "a string with a right side."

#  Print w and e
print(w + e)
