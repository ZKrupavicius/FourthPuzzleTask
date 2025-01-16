from firstpuzzle import count_words_algorithm, count_xmas_words, make_map, read_file


def test_count_of_words():
    x = 1
    y = 0
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        ['X', 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    assert count_words_algorithm(x, y, map_) == 2, "Incorrect amount of MAS words with given coordinates"


def test_count_xmas():
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        ['X', 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    assert count_xmas_words(map_) == 3, "Incorrect count of XMAS words"


def test_make_map():
    first_map = ['MASXA', 'XXMAS']
    result_map = [['M', 'A', 'S', 'X', 'A'], ['X', 'X', 'M', 'A', 'S']]
    assert make_map(first_map) == result_map, "Incorrect creation of the map"

def test_make_from_file_to_list():
    text_file = "input.txt"
    assert type(read_file(text_file)) == list, "Return is not a list"

def test_if_file_empty():
    text_file = "input.txt"
    assert len(read_file(text_file)) != 0, "File is empty"