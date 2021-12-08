with open("input.txt") as file:
    datalist=[int(x) for x in file.read().strip().split(",")]

print(datalist)
mean=sum(datalist)/len(datalist)
print(mean)