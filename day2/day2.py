with open("input.txt") as file:
    datalist=file.read().strip().split("\n")

horizontalposition=0
depth=0

for line in datalist:
    command, argument = line.split(" ")
    argument=int(argument)
    if command=="forward":
        horizontalposition+=argument
    elif command=="down":
        depth+=argument
    elif command=="up":
        depth-=argument

print(f"Horizontal position is {horizontalposition}, depth is {depth}, product is {depth*horizontalposition}")

correctedpos=0
aim=0
correcteddepth=0

for line in datalist:
    command, argument = line.split(" ")
    argument=int(argument)
    if command=="forward":
        correctedpos+=argument
        correcteddepth+=aim*argument
    elif command=="down":
        aim+=argument
    elif command=="up":
        aim-=argument

print(f"Corrected horizontal position is {correctedpos}, depth is {correcteddepth}, product is {correcteddepth*correctedpos}")