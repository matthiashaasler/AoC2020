# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import day_01
import day_02


def print_solutions(day, task_01, task_02):
    print('Solutions for day {}'.format(day))
    print('Solution for task 01: {}'.format(task_01))
    print('Solution for task 02: {}'.format(task_02))
    print(24*'-')
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_01_input = day_01.read_input_file()
    print_solutions('01', task_01=day_01.task_01(day_01_input), task_02=day_01.task_02(day_01_input))
    day_02_input = day_02.read_input_file()
    print_solutions('02', task_01=day_02.task_01(day_02_input), task_02=day_02.task_02(day_02_input))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
