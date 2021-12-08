import time
from collections import Counter 
starttime=time.time()
with open("input.txt") as file:
    datalist=file.read().strip().split("\n")

stringlength=len(datalist[0])

def mostcommonchar(list, pointer):
    charlist=[i[pointer] for i in list]
    charcount=Counter(charlist)
    return charcount.most_common(1)[0][0]

gammarate=''.join([mostcommonchar(datalist,i) for i in range(stringlength)])

epsilonrate=''.join(['1'if i=='0' else '0' for i in gammarate])

powerconsumption=int(gammarate, 2)*int(epsilonrate, 2)

print(f"The power consumption is: {powerconsumption}")

oxygenlist=datalist.copy()

for i in range(stringlength):
    oneslist, zeroeslist=[],[]
    if len(oxygenlist)==1:
        break
    for line in oxygenlist:
        if line[i]=="1":
            oneslist.append(line)
        else:
            zeroeslist.append(line)
    if len(oneslist)>= len(zeroeslist):
        oxygenlist=oneslist.copy()
    else:
        oxygenlist=zeroeslist.copy()

co2list=datalist.copy()

for i in range(stringlength):
    oneslist, zeroeslist=[],[]
    if len(co2list)==1:
        break
    for line in co2list:
        if line[i]=="1":
            oneslist.append(line)
        else:
            zeroeslist.append(line)
    if len(oneslist)>=len(zeroeslist):
        co2list=zeroeslist.copy()
    else:
        co2list=oneslist.copy()

lifesupportrating=int(co2list[0],2)*int(oxygenlist[0],2)

print(f"Life support rating = {lifesupportrating}")
print(f"Total time = {time.time()-starttime}")
