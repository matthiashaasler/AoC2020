def read_input_file():
    with open('input/day_01.inp') as input:
        return [int(i.strip()) for i in input.readlines()]


def task_01(list_of_numbers):
    for i in list_of_numbers:
        for j in list_of_numbers:
            if (i + j) == 2020:
                return i * j


def task_02(list_of_numbers):
    for i in list_of_numbers:
        for j in list_of_numbers:
            for k in list_of_numbers:
                if (i + j + k) == 2020:
                    return i * j * k


if __name__ == '__main__':
    numbers = read_input_file()
    solution_01 = task_01(numbers)
    solution_02 = task_02(numbers)
    print(solution_01, solution_02)