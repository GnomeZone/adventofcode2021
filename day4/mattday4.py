import os
import re
import time
starttime=time.time()
def gridchecker(grid):
    for i in range(5):
        if all(j==1 for j in grid[i*5:i*5+5]):
            return True
        if all(j==1 for j in [grid[i+5*k] for k in range(5)]):
            return True
    return False

def bingochecker(number, card, grid):
    try:
        index=card.index(number)
        grid[index]=1
        return gridchecker(grid)
    except ValueError:
        return False
    


with open("input.txt") as file:
    datalist=file.read().split("\n\n")

bingonumbers=[int(i) for i in datalist[0].split(",")]
height,width=5,5
bingocards=[[int(x) for x in re.split("\W+",i) if x!=""] for i in datalist[1:]]
occupancygrids=[[0 for i in range(25)] for j in datalist[1:]]

BINGO=False
for number in bingonumbers:
    if BINGO==True:
        break
    for i, card in enumerate(bingocards):
        if bingochecker(number, card, occupancygrids[i])==True:
            BINGO=True
            lastnum=number
            cardsum=0
            for j, entry in enumerate(occupancygrids[i]):
                if entry==0:
                    cardsum+=card[j]
            break

print(f"Card sum times last num = {cardsum*lastnum}")

#part 2

occupancygrids=[[0 for i in range(25)] for j in datalist[1:]]

BINGOED=[False for i in datalist[1:]]
for number in bingonumbers:
    if all(BINGOED)==True:
        break
    for i, card in enumerate(bingocards):
        if BINGOED[i]==True:
            continue
        if bingochecker(number, card, occupancygrids[i])==True:
            BINGOED[i]=True
            mostrecentcard=card
            lastnum=number
            mostrecentgrid=occupancygrids[i]

finalcardsum=0
for j, entry in enumerate(mostrecentgrid):
    if entry==0:
        finalcardsum+=mostrecentcard[j]
            

print(f"The score of the last card is {finalcardsum*lastnum}")

