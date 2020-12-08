def read_input_file():
    with open('input/day_02.inp') as input_list:
        return [i.strip() for i in input_list.readlines()]


def task_01(list_of_passwords):
    count_passwords = 0
    for entry in list_of_passwords :
        entry_list = entry.split()
        boundaries = entry_list[0].split('-')
        char = entry_list[1][0]
        password = entry_list[2]

        count_characters = 0
        for character in password:
            if character == char:
                count_characters += 1
        if int(boundaries[0]) <= count_characters <= int(boundaries[1]):
            count_passwords += 1
    return count_passwords


def task_02(list_of_passwords):
    count_passwords = 0
    for entry in list_of_passwords:
        entry_list = entry.split()
        boundaries = entry_list[0].split('-')
        char = entry_list[1][0]
        password = entry_list[2]
        if (char == password[int(boundaries[0]) - 1]) and (char != password[int(boundaries[1]) - 1]):
            count_passwords += 1
        elif (char == password[int(boundaries[1]) - 1]) and (char != password[int(boundaries[0]) - 1]):
            count_passwords += 1
    return count_passwords


if __name__ == '__main__':
    solution_01 = task_01(list_of_passwords=read_input_file())
    solution_02 = task_02(list_of_passwords=read_input_file())
