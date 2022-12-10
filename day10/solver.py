import sys

sys.path.insert(0, "../utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return raw_data.split("\n")


# PART 1
@measure_time
def solve1(data):
    regx = 1
    result = 0
    cycle = 1
    for x in data:
        match x.split():
            case ["noop"]:
                if (cycle + 20) % 40 == 0:
                    result += regx * cycle
                cycle += 1
            case ["addx", value]:
                for i in range(0, 2):
                    if (cycle + 20) % 40 == 0:
                        result += regx * cycle
                    cycle += 1
                regx += int(value)
            case _:
                print("error")

    return result


# PART 2
@measure_time
def solve2(data):
    pass


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
