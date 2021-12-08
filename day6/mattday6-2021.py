import time
starttime=time.time()

with open("input.txt") as file:
    datalist=[int(x) for x in file.read().strip().split(",")]

fishdict={key:0 for key in range(9)}
for i in datalist:
    fishdict[i]+=1

for day in range(256):
    newdict={key:0 for key in range(9)}
    for i in fishdict:
        if i==0:
            newdict[6]+=fishdict[i]
            newdict[8]+=fishdict[i]
        else:
            newdict[i-1]+=fishdict[i]
    fishdict=newdict.copy()
    if day==79:
        sum80=sum(fishdict.values())

sum256=sum(fishdict.values())
print(f"After 80 days, there are {sum80} fish.")
print(f"After 256 days, there are {sum256} fish.")
print(f"Total time = {time.time()-starttime} seconds")
