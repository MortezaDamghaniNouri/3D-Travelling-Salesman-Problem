import random
import math




def list_of_numbers_generator(input_number):
    output_list = []
    i = 0
    while i < input_number:
        output_list.append(i)
        i += 1
    return output_list


# This function returns the euclidean distance between the two input cities
def euclidean_distance_calculator(city_one, city_two):
    return math.sqrt(pow((city_two[0] - city_one[0]), 2) + pow((city_two[1] - city_one[1]), 2) + pow((city_two[2] - city_one[2]), 2))


# This function calculates the fitness of the input chromosomes
def total_distance_calculator(input_chromosome, list_of_cities):
    fitness = 0
    k = 0
    while k < (len(input_chromosome) - 1):
        fitness = fitness + euclidean_distance_calculator(list_of_cities[input_chromosome[k]], list_of_cities[input_chromosome[k + 1]])
        k += 1
    fitness = fitness + euclidean_distance_calculator(list_of_cities[input_chromosome[0]], list_of_cities[input_chromosome[len(input_chromosome) - 1]])
    return fitness


# This function sorts the input list
def sort(input_list):
    k = len(input_list) - 2
    while k >= 0:
        j = 0
        while j <= k:
            if input_list[j][1] > input_list[j + 1][1]:
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
            j += 1

        k = k - 1

    return input_list










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

    if i % 100 == 0:
        print(i)
    i += 1

print("The results list is generated")
print("The len of results: " + str(len(results)))
# print(results)

all_possible_chromosomes = []
i = 0
while i < len(results):
    all_possible_chromosomes.append([results[i], total_distance_calculator(results[i], cities)])
    i += 1

print("Sorting all_possible_chromosomes...")
all_possible_chromosomes = sort(all_possible_chromosomes)

output_file = open("bf_output.txt", "wt")

i = 0
while i < len(all_possible_chromosomes):

    output_file.write(str(round(all_possible_chromosomes[i][1], 5)) + ": " + str(all_possible_chromosomes[i][0].append(all_possible_chromosomes[i][0][0])) + "\n")
    i += 1



output_file.close()































