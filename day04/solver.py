import sys

sys.path.insert(0, "../utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    _parsed = [[x.split(",")[0], x.split(",")[1]] for x in raw_data.split("\n")]
    _splited = [[x[0].split("-"), x[1].split("-")] for x in _parsed]
    _ranged = [
        [range(int(x[0][0]), int(x[0][1]) + 1), range(int(x[1][0]), int(x[1][1]) + 1)]
        for x in _splited
    ]
    return _ranged


# PART 1
@measure_time
def solve1(data):
    i = 0
    for a, b in data:
        seta = set(a)
        setb = set(b)
        setresult = seta & setb
        if setresult == seta or setresult == setb:
            i += 1

    return i


# PART 2
@measure_time
def solve2(data):
    i = 0
    for a, b in data:
        seta = set(a)
        setb = set(b)
        setresult = seta & setb
        if len(setresult) != 0:
            i += 1

    return i


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
