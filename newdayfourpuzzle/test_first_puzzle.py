import pytest

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


@pytest.mark.parametrize("x,y", [("A", 3), pytest.param(0, 4, marks=pytest.mark.xfail), ("X", "P")])
def test_wrong_coordinates_input(x: int, y: int):
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        ['X', 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    with pytest.raises(Exception):
        count_words_algorithm(x, y, map_)


def test_type_of_map_inputs():
    x = 4
    y = 3
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        [1, 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    with pytest.raises(Exception):
        count_words_algorithm(x, y, map_)


@pytest.mark.parametrize("x,y", [(-1, 2), (2, 15), (-1, 12)])
def test_out_of_bounds_coordinates(x: int, y: int):
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        ['X', 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    with pytest.raises(Exception):
        count_words_algorithm(x, y, map_)


def test_count_xmas():
    map_ = [
        ['M', 'X', 'M', 'A', 'S'],
        ['X', 'X', 'M', 'X', 'X'],
        ['S', 'S', 'S', 'A', 'S'],
        ['X', 'M', 'A', 'S', 'S']
    ]
    assert count_xmas_words(map_) == 3, "Incorrect count of XMAS words"


def test_wrong_map():
    map_ = [
        ['M', 'X', 'A'],
        ['X', 'X', 'X']
    ]
    with pytest.raises(Exception):
        count_xmas_words(map_)


def test_empty_map():
    map_ = []
    with pytest.raises(Exception):
        count_xmas_words(map_)


@pytest.mark.parametrize("first_map, result_map",
                         [(['MASXA', 'XXMAS'], [['M', 'A', 'S', 'X', 'A'], ['X', 'X', 'M', 'A', 'S']]),
                          (['MAS', 'XAM'], [['M', 'A', 'S'], ['X', 'A', 'M']]),
                          (pytest.param(['XAM', 'XAM'], [['M', 'S', 'X'], ['X', 'A', 'M']], marks=pytest.mark.xfail))])
def test_make_map(first_map: list, result_map: list):
    assert make_map(first_map) == result_map, "Incorrect creation of the map"


def test_make_from_file_to_list():
    text_file = "input.txt"
    assert type(read_file(text_file)) == list, "Return is not a list"


def test_is_file_empty():
    text_file = "input.txt"
    assert len(read_file(text_file)) > 0, "File is empty"
