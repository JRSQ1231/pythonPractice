# Variable for the number of cars available
cars = 100
# Defines how many seats are in each car.
space_in_a_car = 4.0
# Defines how many drivers a re available
drivers = 30
# Defines how many passengers there are
passengers = 90
# Defines cars not driven as drivers minus the total number of cars available.
cars_not_driven = cars - drivers
# Defines the amount of cars driven as equal to the number of drivers
cars_driven = drivers
# Defines the carpool capacity as equal to the number of cars driven
# multiplied by the number of seats in each car.
carpool_capacity = cars_driven * space_in_a_car
# Defines the average number of passengers in each as the number of
# total passengers divided by the number of cars being driven.
average_passengers_per_car = passengers / cars_driven

# Prints the output.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study drills.  The error mentioned is due to car_pool not being
# equal to carpool.  This creates a different variable.
# Using floating point for space_in_a_car is not necessary because
# you can't have a portion of a whole person or seat in a car.
