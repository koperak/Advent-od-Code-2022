import sys

sys.path.insert(0, "../utils/py")
import utils
import pandas as pd
import re
from collections import deque

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):

    [_header, _instructions] = raw_data.split("\n\n")

    _raw_stacks = pd.Series(_header.split("\n"))
    _stacks = _raw_stacks.str.slice(1, _raw_stacks.str.len()[0], 4)
    _list_of_stacks = [
        deque("".join(_stacks.str.get(x)[:-1].str.replace(" ", "")))
        for x, d in enumerate(_stacks.str)
    ]

    _instruction_list = [
        re.findall(r"(\d+)", _instruction) for _instruction in _instructions.split("\n")
    ]

    return [_list_of_stacks, _instruction_list]


def move_crates(move_from, move_to, _crates):
    """FILO move number of crates from deque to another deque
    input: move_from - deque from which number of elements will be pop'ed
    input: move_to - quegue to which number of elements wil be append'ed
    WARNINIG - this is bad code because move_from, move_to are external data structures
               modified within this function, one big problem is that I can't control
               data creation and in effect some data left within move_too, move_from
    """
    for i in range(0, _crates):
        move_to.appendleft(move_from.popleft())
    print(move_to)

def move_crates_v9001(move_from, move_to, _crates):
    """FILO move number of crates from deque to another deque
    input: move_from - deque from which number of elements will be pop'ed
    input: move_to - quegue to which number of elements wil be append'ed
    """
    print(f'START:\tfrom: {move_from}, to: {move_to}')

    _a = ''
    for i in range(0, _crates):
        _a = _a + move_from.popleft()
    [move_to.appendleft(_elem) for _elem in reversed(_a)]
    
    print(f'END:\tfrom: {move_from}, to: {move_to}')


# PART 1
@measure_time
def solve1(data):
    [
        move_crates(
            data[0][int(_step[1]) - 1], data[0][int(_step[2]) - 1], int(_step[0])
        )
        for _step in data[1]
    ]

    return ''.join([_crate_id.popleft() for _crate_id in data[0]])


# PART 2
@measure_time
def solve2(data):

    #print(f'STACKI: {data[0]}\nINSTRUKCJE: {data[1]}')

    for _step in data[1]:
        print(f'STEP: {_step}, INPUT: {data[0][int(_step[1]) - 1], data[0][int(_step[2]) - 1], int(_step[0])}')
        move_crates_v9001(
            data[0][int(_step[1]) - 1], data[0][int(_step[2]) - 1], int(_step[0])
        )

    return ''.join([_crate_id.popleft() for _crate_id in data[0]])


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1 Data : {data}")

    """ Problem lies in here - I'm using mutable 'data' structure which is modified
        in Part 1 and left in memoru to use on Part 2 
        How to solve this exercise whit functional Python code?   
    """
    data = parse(open("input.txt").read().strip())
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
