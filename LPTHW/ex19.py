# creates the function "Cheese_and_Crackers".
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# This way inputs the 20, and 30, directly in to the "cheese_count" 
# and "boxes_of_crackers" variables.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# This way inputs variables, in to the arguements.  "amount_of_cheese for
# "Cheese_count", and "amount_of_crackers" for "boxes_of_crackers", and defines 
# those variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This way passes the two arguements as math problems, separated by a comma to
# tell the function which is the first and which is the second arguement
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

# Fairly self explanatory.  Two arguements, using the variables from the previous
# example, and adding to them.
print("And we can combnine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)