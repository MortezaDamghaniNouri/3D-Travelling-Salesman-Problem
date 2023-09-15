import random
import math
# This function generates some random chromosomes. The size of the chromosome is given as an input
def random_chromosome_generator(size):
    output_list = []
    k = 0
    while k < size:
        random_number = random.randint(0, (size - 1))
        if len(output_list) == 0:
            output_list.append(random_number)
        else:
            if random_number not in output_list:
                output_list.append(random_number)
            else:
                while True:
                    new_random_number = random.randint(0, (size - 1))
                    if new_random_number not in output_list:
                        output_list.append(new_random_number)
                        break
        k += 1
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


# This function generates the first generation of chromosomes
def first_generation_generator(input_population_number, input_number_of_cities, input_list_of_cities):
    output_list = []
    number_of_all_possibilities = math.factorial(input_number_of_cities)
    if number_of_all_possibilities >= input_population_number:
        k = 0
        while k < input_population_number:
            random_chromosome = random_chromosome_generator(input_number_of_cities)
            if random_chromosome not in output_list:
                output_list.append(random_chromosome)
            else:
                while True:
                    new_random_chromosome = random_chromosome_generator(input_number_of_cities)
                    if new_random_chromosome not in output_list:
                        output_list.append(new_random_chromosome)
                        break

            k += 1

    else:
        k = 0
        while k < number_of_all_possibilities:
            random_chromosome = random_chromosome_generator(input_number_of_cities)
            if random_chromosome not in output_list:
                output_list.append(random_chromosome)
            else:
                while True:
                    new_random_chromosome = random_chromosome_generator(input_number_of_cities)
                    if new_random_chromosome not in output_list:
                        output_list.append(new_random_chromosome)
                        break

            k += 1

        subtraction = input_population_number - number_of_all_possibilities
        k = 0
        while k < subtraction:
            random_chromosome = random_chromosome_generator(input_number_of_cities)
            output_list.append(random_chromosome)
            k += 1

    k = 0
    new_output_list = []
    while k < len(output_list):
        temp_list = [output_list[k]]
        temp_list.append(total_distance_calculator(temp_list[0], input_list_of_cities))
        new_output_list.append(temp_list)
        k += 1

    return new_output_list


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


# This function considers whether the input element exists in the input list or not
def does_exist(input_element, input_list):
    n = 0
    while n < len(input_list):
        if input_element == input_list[n][0]:
            return n, input_list[n][1]
        if input_element == input_list[n][1]:
            return n, input_list[n][0]
        n += 1






# Crossover operation is implemented in this function
def crossover(input_parent_one, input_parent_two, input_number_of_cities):
    while True:
        random_cut_one = random.randint(1, input_number_of_cities - 1)
        random_cut_two = random.randint(1, input_number_of_cities - 1)
        if random_cut_one != random_cut_two:
            break
    if random_cut_one > random_cut_two:
        lower_cut = random_cut_two
        upper_cut = random_cut_one
    else:
        lower_cut = random_cut_one
        upper_cut = random_cut_two
    offspring_one = []
    offspring_two = []
    k = 0
    while k < input_number_of_cities:
        offspring_one.append(-1)
        offspring_two.append(-1)
        k += 1

    k = lower_cut
    map_list = []
    offspring_list_one = []
    offspring_list_two = []
    while k < upper_cut:
        offspring_one[k] = input_parent_two[k]
        offspring_list_one.append(input_parent_two[k])
        offspring_two[k] = input_parent_one[k]
        offspring_list_two.append(input_parent_one[k])

        # generating the map list
        map_list.append([input_parent_one[k], input_parent_two[k]])
        k += 1

    # generating the remaining of offspring one
    k = 0
    while k < lower_cut:

        if input_parent_one[k] not in offspring_list_one:
            offspring_one[k] = input_parent_one[k]
        else:
            temp_list = []
            j = 0
            while j < len(map_list):
                temp_list.append(map_list[j])
                j += 1

            element = input_parent_one[k]
            while True:
                index, element = does_exist(element, temp_list)
                if element not in offspring_list_one:
                    offspring_one[k] = element
                    break
                else:
                    temp_list.pop(index)
        k += 1

    k = upper_cut
    while k < input_number_of_cities:

        if input_parent_one[k] not in offspring_list_one:
            offspring_one[k] = input_parent_one[k]
        else:
            temp_list = []
            j = 0
            while j < len(map_list):
                temp_list.append(map_list[j])
                j += 1

            element = input_parent_one[k]
            while True:
                index, element = does_exist(element, temp_list)
                if element not in offspring_list_one:
                    offspring_one[k] = element
                    break
                else:
                    temp_list.pop(index)
        k += 1


    # generating the remaining of offspring two
    k = 0
    while k < lower_cut:

        if input_parent_two[k] not in offspring_list_two:
            offspring_two[k] = input_parent_two[k]
        else:
            temp_list = []
            j = 0
            while j < len(map_list):
                temp_list.append(map_list[j])
                j += 1

            element = input_parent_two[k]
            while True:
                index, element = does_exist(element, temp_list)
                if element not in offspring_list_two:
                    offspring_two[k] = element
                    break
                else:
                    temp_list.pop(index)
        k += 1

    k = upper_cut
    while k < input_number_of_cities:

        if input_parent_two[k] not in offspring_list_two:
            offspring_two[k] = input_parent_two[k]
        else:
            temp_list = []
            j = 0
            while j < len(map_list):
                temp_list.append(map_list[j])
                j += 1

            element = input_parent_two[k]
            while True:
                index, element = does_exist(element, temp_list)
                if element not in offspring_list_two:
                    offspring_two[k] = element
                    break
                else:
                    temp_list.pop(index)
        k += 1




    print("upper cut: " + str(upper_cut))
    print("lower cut: " + str(lower_cut))
    return offspring_one, offspring_two


# Mutation is implemented in this function
def mutation(input_chromosome, input_number_of_cities):
    random_number = random.randint(1, 10)
    mutation_probability = 2
    if random_number <= mutation_probability:
        while True:
            first_random_index = random.randint(0, (input_number_of_cities - 1))
            second_random_index = random.randint(0, (input_number_of_cities - 1))
            if first_random_index != second_random_index:
                temp = input_chromosome[first_random_index]
                input_chromosome[first_random_index] = input_chromosome[second_random_index]
                input_chromosome[second_random_index] = temp
                break
        return input_chromosome
    else:
        return input_chromosome















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

# generating the first generation
number_of_population = 500
population = first_generation_generator(number_of_population, number_of_cities, cities)
population = sort(population)
# print(population)
# print(number_of_cities)

if number_of_cities > 2:
    print(crossover([3, 7, 5, 2, 4, 1, 6], [4, 2, 3, 5, 1, 7, 6], number_of_cities))




















