from firstpuzzle import count_words_algorithm, count_xmas_words, make_map


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
