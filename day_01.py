from input.return_input import read_input_file


def task_01():
    list_of_numbers = [int(i.strip()) for i in read_input_file('input/day_01.inp')]
    for i in list_of_numbers:
        for j in list_of_numbers:
            if (i + j) == 2020:
                return i * j


def task_02():
    list_of_numbers = [int(i.strip()) for i in read_input_file('input/day_01.inp')]
    for i in list_of_numbers:
        for j in list_of_numbers:
            for k in list_of_numbers:
                if (i + j + k) == 2020:
                    return i * j * k


if __name__ == '__main__':
    numbers = read_input_file()
    solution_01 = task_01()
    solution_02 = task_02()
    print(solution_01, solution_02)
