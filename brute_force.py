import random
import math




def list_of_numbers_generator(input_number):
    output_list = []
    i = 1
    while i <= input_number:
        output_list.append(i)
        i += 1
    return output_list















# reading from the input file
input_file = open("input.txt", "rt")
lines = []
while True:
    line = input_file.readline()
    if line == "":
        break
    lines.append(line.rstrip())
input_file.close()

new_lines = []
for i in lines:
    if i != "":
        new_lines.append(i)

lines = new_lines

# parsing the lines of the input file
cities = []
number_of_cities = int(lines[0])
i = 1
while i < len(lines):
    temp_list = lines[i].split(" ")
    j = 0
    while j < len(temp_list):
        temp_list[j] = int(temp_list[j])
        j += 1
    cities.append(temp_list)
    i += 1


results = []
i = 1
while i <= math.factorial(number_of_cities):
    while True:
        list_of_numbers = list_of_numbers_generator(number_of_cities)
        result = []
        while len(list_of_numbers) != 0:
            random_number = random.randint(0, (len(list_of_numbers) - 1))
            result.append(list_of_numbers[random_number])
            list_of_numbers.pop(random_number)
        if result not in results:
            results.append(result)
            break
    print(i)
    i += 1

print("the len of results: " + str(len(results)))
print(results)














































