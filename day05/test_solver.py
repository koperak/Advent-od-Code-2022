import pytest

from solver import parse, solve1, solve2, move_crates, move_crates_v9001
from collections import deque

TESTDATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_move_crates():
    crate1 = deque("NZ")
    crate2 = deque("DCM")
    crate3 = deque("P")
    move_crates(crate2, crate1, 1)
    assert crate1 == deque("DNZ")

    move_crates(crate1, crate3, 3)
    assert crate1 == deque("")
    assert crate2 == deque("CM")

    move_crates(crate2, crate1, 2)
    assert crate1 == deque("MC")

    move_crates(crate1, crate2, 1)
    assert crate1 == deque("C")
    assert crate2 == deque("M")
    assert crate3 == deque("ZNDP")

def test_move_crates_v9001():
    crate1 = deque("NZ")
    crate2 = deque("DCM")
    crate3 = deque("P")
    
    move_crates_v9001(crate2, crate1, 1)
    assert crate1 == deque("DNZ")
    assert crate2 == deque("CM")
    assert crate3 == deque("P")

    move_crates_v9001(crate1, crate3, 3)
    assert crate1 == deque("")
    assert crate2 == deque("CM")
    assert crate3 == deque("DNZP")

    move_crates_v9001(crate2, crate1, 2)
    assert crate1 == deque("CM")
    assert crate2 == deque("")
    assert crate3 == deque("DNZP")

    move_crates_v9001(crate1, crate2, 1)
    assert crate1 == deque("M")
    assert crate2 == deque("C")
    assert crate3 == deque("DNZP")


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == "CMZ"


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    assert solution == "MCD"
