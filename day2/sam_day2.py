import pandas as pd
import time
start = time.time()

data = pd.read_csv("input.txt", delimiter=" ", names=["Direction", "Number"])    # read input as dataframe

# part 1
x_pos, depth = 0, 0
for i in data:
    print(i)

for i in range(len(data["Direction"])):
    if data["Direction"][i] == "forward":
        x_pos += data["Number"][i]
    elif data["Direction"][i] == "down":
        depth += data["Number"][i]
    elif data["Direction"][i] == "up":
        depth -= data["Number"][i]

print(f"Horizontal position is {x_pos}, depth is {depth})")
print(f"Result of positions multiplied is: {x_pos*depth}")

# part 2
x_pos2 = 0
depth2 = 0
aim = 0

for i in range(len(data["Direction"])):
    if data["Direction"][i] == "forward":
        x_pos2 += data["Number"][i]
        depth2 += aim * data["Number"][i]
    elif data["Direction"][i] == "down":
        aim += data["Number"][i]
    elif data["Direction"][i] == "up":
        aim -= data["Number"][i]

print(f"Corrected horizontal position is {x_pos2}, corrected depth is {depth2})")
print(f"Result of corrected positions multiplied is: {x_pos2*depth2}")

print(f"Time elapsed: {time.time()-start} s")