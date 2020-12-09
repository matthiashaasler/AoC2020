# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from days import day_03, day_02, day_01


def print_solutions(day, task_01, task_02):
    print('Solutions for day {}'.format(day))
    print('Solution for task 01: {}'.format(task_01))
    print('Solution for task 02: {}'.format(task_02))
    print(24*'-')



    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_solutions('01', task_01=day_01.task_01(), task_02=day_01.task_02())
    print_solutions('02', task_01=day_02.task_01(), task_02=day_02.task_02())
    print_solutions('03', task_01=day_03.task_01(), task_02=day_03.task_02())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
