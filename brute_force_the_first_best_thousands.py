"""
This programs generates the first 1000 shortest paths for solving Traveling Salesman Problem.
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


# This function finds and returns the best thousands chromosomes based on the input number
def thousands_best_chromosomes_finder(input_chromosomes_list, number_of_bests):
    output_list = []
    counter = 0
    while counter < number_of_bests:
        minimum = input_chromosomes_list[0][1]
        index = 0
        i = 1
        while i < len(input_chromosomes_list):
            if input_chromosomes_list[i][1] < minimum:
                minimum = input_chromosomes_list[i][1]
                index = i
            i += 1
        output_list.append(input_chromosomes_list[index])
        input_chromosomes_list.pop(index)
        if counter % 10 == 0:
            print(counter)
        counter += 1

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




all_possible_chromosomes = list(permutations(list_of_numbers_generator(number_of_cities), number_of_cities))
print("The number of cities: " + str(number_of_cities))
print("The number of all permutations: " + str(len(all_possible_chromosomes)))

total_population = []
i = 0
while i < len(all_possible_chromosomes):
    total_population.append([list(all_possible_chromosomes[i]), total_distance_calculator(list(all_possible_chromosomes[i]), cities)])
    i += 1

print("finding the best thousands of chromosomes...")
number_of_the_best_desired_chromosomes = 100
the_first_thousands_chromosomes = thousands_best_chromosomes_finder(total_population, number_of_the_best_desired_chromosomes)
print("The length of the_first_thousands_chromosomes: " + str(len(the_first_thousands_chromosomes)))
output_file = open("the_thousands_best_output.txt", "wt")

i = 0
while i < len(the_first_thousands_chromosomes):
    the_first_thousands_chromosomes[i][0].append(the_first_thousands_chromosomes[i][0][0])
    output_file.write(str(round(the_first_thousands_chromosomes[i][1], 3)) + ": " + str(the_first_thousands_chromosomes[i][0]) + "\n")
    i += 1



output_file.close()
print("the_thousands_best_output.txt generated.")












