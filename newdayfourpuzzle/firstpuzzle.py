from pathlib import Path
from typing import List


def read_file(file_path: str) -> List[str]:

    file = Path(file_path)
    if not file.is_file():
        raise Exception ("File not found")
    with file.open('r') as f:
        lines = f.readlines()
    return lines


def make_map(first_input_lines: List) -> List[str]:
    correct_lines = first_input_lines.copy()
    for index, line in enumerate(correct_lines):
        line: str = line.replace("\n", "")
        correct_lines[index] = list(line)
    return correct_lines


def count_xmas_words(map_: List) -> int:
    count = 0
    for y, row in enumerate(map_):
        for x, value in enumerate(row):
            if value != 'X':
                continue
            count += count_words_algorithm(x, y, map_)
    return count


def count_words_algorithm(x, y, map_) -> int:
    total_count = 0
    x0 = x + 1
    x0minus = x - 1
    y0 = y + 1
    y0minus = y - 1
    x1 = x + 4
    x1minus = x - 4
    y1 = y + 4
    y1minus = y - 4

    coordinates = [
        ([y] * 3, list(range(x0, x1))),
        (list(range(y0, y1)), list(range(x0, x1))),
        (list(range(y0, y1)), [x] * 3),
        (list(range(y0, y1)), list(range(x0minus, x1minus, -1))),
        ([y] * 3, list(range(x0minus, x1minus, -1))),
        (list(range(y0minus, y1minus, -1)), list(range(x0minus, x1minus, -1))),
        (list(range(y0minus, y1minus, -1)), [x] * 3),
        (list(range(y0minus, y1minus, -1)), list(range(x0, x1)))
    ]

    for y_coordinates, x_coordinates in coordinates:
        buffer = []
        for idx in range(3):
            new_y = y_coordinates[idx]
            new_x = x_coordinates[idx]
            if new_y not in range(0, len(map_)) or new_x not in range(0, len(map_[0])):
                break
            buffer.append(map_[new_y][new_x])
        total_count += "".join(buffer) == "MAS"
    return total_count


if __name__ == "__main__":
    f_lines = read_file("input.txt")
    print(f_lines)
    mapp = make_map(f_lines)
    print(mapp)
    count_words = count_xmas_words(mapp)
    print(count_words)
