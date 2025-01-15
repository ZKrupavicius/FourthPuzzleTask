from pathlib import Path
from typing import List


def read_file(file_path) -> List[str]:
    file = Path(file_path)
    with file.open('r') as f:
        lines = f.readlines()
    return lines


def make_map(correct_lines) -> List[str]:
    for index, line in enumerate(correct_lines):
        line = list(line)
        correct_lines[index] = line
    return correct_lines


def count_xmas_words(map_) -> int:
    count = 0
    for y, row in enumerate(map_):
        for x, value in enumerate(row):
            if value != 'X':
                continue
            count += check_if_direction_is_in_bounds(x, y, map_)
    return count


def check_for_mas(buffer) -> int:
    counter = 0
    if ''.join(buffer) == 'MAS':
        counter += 1
    return counter


def check_if_direction_is_in_bounds(x, y, map_) -> int:
    buffer_of_mas_string = []
    total_count = 0

    for i in range(x + 1, x + 4):
        if i < len(map_):
            buffer_of_mas_string.append(map_[y][i])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(x - 1, x - 4, -1):
        if i >= 0:
            buffer_of_mas_string.append(map_[y][i])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(y + 1, y + 4):
        if i < len(map_):
            buffer_of_mas_string.append(map_[i][x])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(y - 1, y - 4, -1):
        if i >= 0:
            buffer_of_mas_string.append(map_[i][x])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(1, 4):
        if x + i < len(map_) and y + i < len(map_):
            buffer_of_mas_string.append(map_[y + i][x + i])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(1, 4):
        if x - i >= 0 and y - i >= 0:
            buffer_of_mas_string.append(map_[y - i][x - i])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(1, 4):
        if x + i < len(map_) and y - i >= 0:
            buffer_of_mas_string.append(map_[y - i][x + i])
    total_count += check_for_mas(buffer_of_mas_string)
    buffer_of_mas_string = []

    for i in range(1, 4):
        if x - i >= 0 and y + i < len(map_):
            buffer_of_mas_string.append(map_[y + i][x - i])
    total_count += check_for_mas(buffer_of_mas_string)

    return total_count

    # container [((y,y1,y2), range(x, x1,x2)), ()]


if __name__ == "__main__":
    f_lines = read_file("input.txt")
    count_words = count_xmas_words(make_map(f_lines))
    print(count_words)
