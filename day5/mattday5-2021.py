import time
starttime=time.time()
with open("input.txt") as file:
    datalist=file.read().strip().split("\n")

cleanedata=[i.split(" -> ") for i in datalist]
visitedpoints={}

def valdicttrier(xaddress,yaddress, dictionary):
    try:
        dictionary[xaddress,yaddress]+=1
    except KeyError:
        dictionary[xaddress,yaddress]=1

for vals in cleanedata:
    x1,y1=[int(i) for i in vals[0].split(",")]
    x2,y2=[int(i) for i in vals[1].split(",")]
    if x1==x2:
        if y2>y1:
            for i in range(y1, y2+1):
                valdicttrier(x1,i, visitedpoints)
        elif y1>y2:
            for i in range(y2, y1+1):
                valdicttrier(x1,i, visitedpoints)
    elif y1==y2:
        if x2>x1:
            for i in range(x1, x2+1):
                valdicttrier(i,y1, visitedpoints)
        elif x1>x2:
            for i in range(x2, x1+1):
                valdicttrier(i,y1, visitedpoints)

multiplecounter=0

for i in visitedpoints:
    if visitedpoints[i]>1:
        multiplecounter+=1

print(f"The number of points with multiple vents is {multiplecounter}")

#part2

visitedpoints={}
for vals in cleanedata:
    x1,y1=[int(i) for i in vals[0].split(",")]
    x2,y2=[int(i) for i in vals[1].split(",")]
    if x1==x2:
        if y2>y1:
            for i in range(y1, y2+1):
                valdicttrier(x1,i, visitedpoints)
        elif y1>y2:
            for i in range(y2, y1+1):
                valdicttrier(x1,i, visitedpoints)
    elif y1==y2:
        if x2>x1:
            for i in range(x1, x2+1):
                valdicttrier(i,y1, visitedpoints)
        elif x1>x2:
            for i in range(x2, x1+1):
                valdicttrier(i,y1, visitedpoints)
    else:
        if y2>y1:
            if x2>x1:
                for i in range(x2-x1+1):
                    valdicttrier(x1+i,y1+i, visitedpoints)
            if x1>x2:
                for i in range(x1-x2+1):
                    valdicttrier(x1-i, y1+i, visitedpoints)
        elif y1>y2:
            if x2>x1:    
                for i in range(x2-x1+1):
                    valdicttrier(x1+i, y1-i, visitedpoints)
            if x1>x2:
                for i in range(x1-x2+1):
                    valdicttrier(x1-i, y1-i, visitedpoints)

multiplecounter=0

for i in visitedpoints:
    if visitedpoints[i]>1:
        multiplecounter+=1
print(f"Including diagonals, the numbers of points with multiple vents is {multiplecounter}")
print(f"Total time = {time.time()-starttime}")
