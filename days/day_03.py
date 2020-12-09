from input.return_input import read_input_file


def task_00(y_step=None, x_step=None):
    map = [i.strip() for i in read_input_file('input/day_03.inp')]
    length_of_map = len(map)
    y_position = 0
    x_position = 0
    tree_count = 0
    while y_position < length_of_map:
        if x_position > len(map[y_position]) - 1:
            x_position = x_position - len(map[y_position])
        if map[y_position][x_position] == '#':
            tree_count += 1
        y_position += y_step
        x_position += x_step
    return tree_count


def task_01():
    return task_00(y_step=1, x_step=3)


def task_02():
    return task_00(y_step=1, x_step=1) * task_00(y_step=1, x_step=3) * task_00(y_step=1, x_step=5) \
           * task_00(y_step=1, x_step=7) * task_00(y_step=2, x_step=1)


if __name__ == '__main__':
    print(task_01())
