with open("input.txt") as file:
    datalist=file.read().strip().split("\n")

datalist=[int(i) for i in datalist]

increasedcount=0
for i in range(len(datalist)-1):
    if datalist[i+1]>=datalist[i]:
        increasedcount+=1




print(f"{increasedcount} measurements are higher than the previous")
averageincreasedcount=0

for i in range(len(datalist)-3):
    if sum(datalist[i+1:i+4])>sum(datalist[i:i+3]):
        averageincreasedcount+=1

print(f"The average increased count was {averageincreasedcount}")
