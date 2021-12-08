import time
start = time.time()

def most_common(lst):
    """Find most common occurrence in a list."""
    return max(set(lst), key=lst.count)


with open("input.txt") as file:
    data = file.read().strip().split("\n")

string_length = len(data[0])

array=[]
for row in data:
    array.append([char for char in row])

# part 1
gamma_string = ""
epsilon_string = "1" * string_length
for i in range(string_length):
    char = most_common([row[i] for row in array])
    gamma_string += char

epsilon_string = str(int(epsilon_string) - int(gamma_string))

gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)

print(f"Gamma = {gamma}, Epsilon = {epsilon}, power consumption is {gamma*epsilon}")

# part 2
array2 = array.copy()
array3 = array.copy()

for i in range(string_length):
    char = most_common([row[i] for row in array2])
    array2 = [elem for elem in array2 if elem[i] == char]
    if len(array) == 1:
        break

oxygen_string = ""
for i in range(len(array2[0])):
    oxygen_string += array2[0][i]

for i in range(string_length):
    char = str(1 - int(most_common([row[i] for row in array3])))
    array3 = [elem for elem in array3 if elem[i] == char]
    if len(array3) == 1:
        break

co2_string = ""
for i in range(len(array3[0])):
    co2_string += array3[0][i]

oxygen = int(oxygen_string, 2)
co2 = int(co2_string, 2)

print(f"Oxygen rating = {oxygen}, CO2 rating= {co2}, life support rating is {oxygen*co2}")

print(f"Time elapsed: {time.time()-start} s")
