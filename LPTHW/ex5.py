name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches_to_cent = 2.54
pounds_to_kilos = .453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {round(height * inches_to_cent,1)} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {round(weight * pounds_to_kilos,2)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, {weight} I get {total}.")
