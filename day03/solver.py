import sys
from string import ascii_letters

sys.path.insert(0, "../utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [x for x in raw_data.split("\n")]

# PART 1
@measure_time
def solve1(data):
    _unique_values = [set(x[:len(x)//2])&set(x[len(x)//2:]) for x in data]
    return sum(ascii_letters.index(x.pop())+1 for x in _unique_values)


# PART 2
@measure_time
def solve2(data):
    _trilines = [data[i:i + 3] for i in range(0, len(data), 3)]
    _unique_values = [set(x) & set(y) & set(z) for x,y,z in _trilines]
    return sum(ascii_letters.index(x.pop())+1 for x in _unique_values)


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))

