"""
In this program, Brute Force is implemented using itertools library in Python.
By generating all of the possible permutations, the shortest path for solving Traveling Salesman Problem is found for testing the result of main.py.
"""


from itertools import permutations
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


        if k % 1000 == 0:
            print(k)
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




all_possible_chromosomes = list(permutations(list_of_numbers_generator(number_of_cities), number_of_cities))
print("The number of cities: " + str(number_of_cities))
print("The number of all permutations: " + str(len(all_possible_chromosomes)))

total_population = []
i = 0
while i < len(all_possible_chromosomes):
    total_population.append([list(all_possible_chromosomes[i]), total_distance_calculator(list(all_possible_chromosomes[i]), cities)])
    i += 1

print("Sorting the population...")
total_population = sort(total_population)

output_file = open("itertools_output.txt", "wt")

i = 0
while i < len(total_population):
    total_population[i][0].append(total_population[i][0][0])
    output_file.write(str(round(total_population[i][1], 3)) + ": " + str(total_population[i][0]) + "\n")
    i += 1



output_file.close()

print("itertools_output.txt generated.")




































