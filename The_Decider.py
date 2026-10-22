import random
import re

choices = []

choice1 = (input("What is one of the choices? (You may add multiple choices separated by a comma)\n"))
if "," in choice1:
    temp_arr = choice1.split(",")
    for word in temp_arr:
        choices.append(word)
else:
    choices.append(choice1)

choice2 = (input("\nSecond Choice?\n"))
if "," in choice2:
    temp_arr = choice2.split(",")
    for word in temp_arr:
        choices.append(word)
else:
    choices.append(choice2)


i = 0
while i < 1000:
    print()
    n = input("Any more? (Type 'end' to get your result)\n")
    if re.search("^end$", n, re.IGNORECASE):
        break
    choices.append(n)
    i += 1
    
print("\n")

print(f"I've decided on this: {random.choice(choices)}\n\n")

input("Deal with it. Press ENTER to Exit")