a={}

try:
    a[1,2]+=1
except KeyError:
    a["b"]=1

a[[1,2]]=1
for i in range(5,10):
    print(i)
print(a)