import pytest
from solver import parse, solve1, solve2

TESTDATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 24000


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    assert solution == 45000