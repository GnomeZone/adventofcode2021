import enum


def a(b):
    b[1]=2

b=[1,1,1,1,1,2,3,4,1,2]

print(b[0:5])
a(b)
print(b)

b=[1,2,3,4,5,6]

for index, val in enumerate(b):
    print(val)
    if index==3:
        b.pop(index)

