# Function to retrieve data
def an_elf():
    file = open("data.txt", "r")
    data = []
    for line in file.readlines():
        data.append(line.replace('\n', ''))

    calorie_set = []
    calorie_list = []
    is_an_elf = True

    for element in data:

        if element != '':
            # creating sets (list)
            calorie_set.append(int(element))
        else:
            # nesting the set (list) into the the main list
            calorie_list.append(calorie_set)
            # restart the process to create another set
            calorie_set = []
    # return the main list with nested lists (each set belongs to a different elf)
    return calorie_list


# 2 Function to calculate calories
# calorie_list: list
def calculate_calories(calorie_list):
    total_calories_list = []

    # calulate the calories of every set of calories nested in the argument
    for calorie_set in calorie_list:
        total_calories = 0
        for element in calorie_set:
            total_calories = total_calories + element
        total_calories_list.append(total_calories)
    # this list contains a nested lists, each list nest has the the value of each previous set
    return total_calories_list

# 3 Function that prints the highest value
# calorie_values : list
def elf_with_most_calories(calorie_values):
    calorie_values.sort()

    # print the highest value
    # print("The elf with the most calories has : ", calorie_values[-1], "calories")

    # sum of the last three highest values
    print(calorie_values[-3] + calorie_values[-2] + calorie_values[-1])

# calling the function to retrieve the main list with nested list calories each elf is carrying
calorie_list = an_elf()
# caluclating the values of each nested list
calories = calculate_calories(calorie_list)
# verifying which elf has is carrying the moost calories
elf_with_most_calories(calories)
