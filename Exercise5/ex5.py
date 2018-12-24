name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_per_inch = 2.54
kg_per_pound = 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height*cm_per_inch} cm tall.")
print(f"He's {weight*kg_per_pound} kg heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height*cm_per_inch + weight*kg_per_pound
print(f"If I add {age}, {height*cm_per_inch}, and {weight*kg_per_pound} I get {total}.")
