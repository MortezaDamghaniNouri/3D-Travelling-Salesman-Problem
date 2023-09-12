import random

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
















# reading from the input file
input_file = open("input.txt", "rt")
lines = []
while True:
    line = input_file.readline()
    if line == "":
        break
    lines.append(line.rstrip())
input_file.close()

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
number_of_population = 1000
population = []
i = 1

j = 0
while j < 6:
    print(random_chromosome_generator(5))
    j += 1



# while i <= number_of_population:
#     temp_list = [random_chromosome_generator(number_of_cities)]
#     temp_list.append(fitness_calculator(temp_list[0]))
#
#
#
#     i += 1




















