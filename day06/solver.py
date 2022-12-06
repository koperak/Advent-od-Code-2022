import sys
from collections import deque

sys.path.insert(0, "../utils/py")
import utils


measure_time = utils.stopwatch()


def sliding_window(_data_string, _window_size):
    i = 0

    q = deque(_data_string[: _window_size + i])

    for i, _ in enumerate(_data_string):
        _character = _data_string[_window_size + i : _window_size + 1 + i]
        q.popleft()
        q.append(_character)
        if len(set(q)) == len(q):
            break

    return i + _window_size + 1


@measure_time
def parse(raw_data):
    return raw_data


# PART 1
@measure_time
def solve1(data):
    return sliding_window(data, 4)


# PART 2
@measure_time
def solve2(data):
    return sliding_window(data, 14)


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
