

# reading from the input file
input_file = open("input.txt", "rt")
lines = []
while True:
    line = input_file.readline()
    if line == "":
        break
    lines.append(line)
input_file.close()

# parsing the lines of the input file
cities = []
number_of_cities = lines[0]
i = 1
while i < len(lines):
    temp_list = lines[i].split(" ")
    cities.append(temp_list)
    i += 1


print(number_of_cities)
for i in cities:
    print(i)




