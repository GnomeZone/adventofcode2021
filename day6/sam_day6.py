import time
import numpy as np

start = time.time()

with open("input.txt") as file:
    data = file.read().strip().split(",")

data = np.array(data, dtype=int)

fish_array = np.zeros(9, dtype=np.longlong)

for i in data:
    fish_array[i] += 1

for i in range(256):
    new_fish_array = np.zeros(fish_array.shape, dtype=np.longlong)
    for j in range(len(fish_array)):
        if j == 0:
            new_fish_array[6] += fish_array[j]
            new_fish_array[8] += fish_array[j]
        else:
            new_fish_array[j-1] += fish_array[j]
    fish_array = new_fish_array.copy()
    if i == 79:
        print(f"Number of fish after 80 days: {np.sum(fish_array)}")

print(f"Number of fish after 256 days: {np.sum(fish_array)}")

print(f"Time elapsed: {time.time()-start} s")
