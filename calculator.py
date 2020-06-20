import re

print("Our Magical Calculator is going to be strated!")
print("Type 'quit' if you want to exit","\n")

previous = 0
run = True

def performMatch():
    global run
    global previous

    if previous == 0:
        equation = input("Enter your equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
        print("Goodbye Human!")
    else:
        equation = re.sub('[a-zA-Z,.:()=" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)
        print("you typed", previous)

while run:
    performMatch()