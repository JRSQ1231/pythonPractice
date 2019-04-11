from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Just for giggles, here it is:", fourth)
fifth = input("Type something here:")
print(fifth)
