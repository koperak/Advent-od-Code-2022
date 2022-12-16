import sys
from typing import Any, Generator
import parse as external_parse

sys.path.insert(0, "../utils/py")
import utils


class Monkey:
    def __init__(
        self, monkey_id, starting_items, operation, divisible_by, test_true, test_false, worry_level_divider
    ) -> None:
        self.monkey_id = int(monkey_id)
        self.starting_items = list(map(int, starting_items.replace(",", "").split()))
        self.operation = operation
        self.divisible_by = int(divisible_by)
        self.test_true = int(test_true)
        self.test_false = int(test_false)
        self.items_inspected = 0
        self.worry_level_divider = worry_level_divider

    def inspect_items(self) -> Generator[tuple[Any, int], None, None]:

        while self.starting_items:
            self.items_inspected += 1
            new = eval(self.operation.replace("old", str(self.starting_items.pop())))
            worry_level = new // self.worry_level_divider

            if worry_level % self.divisible_by == 0:
                pass_to_monkey_id = self.test_true
            else:
                pass_to_monkey_id = self.test_false

            yield pass_to_monkey_id, worry_level


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):

    RE_MONKEY = "Monkey {monkey_id}:\n  Starting items: {starting_items}\n  Operation: new = {operation}\n  Test: divisible by {divisible_by}\n    If true: throw to monkey {test_true}\n    If false: throw to monkey {test_false}"
    re_monkey = external_parse.compile(RE_MONKEY)

    return [
        re_monkey.parse(monkey_text) for monkey_text in raw_data.split("\n\n")
    ]


# PART 1
@measure_time
def solve1(data):
    monkeys = [
        Monkey(
            item["monkey_id"],
            item["starting_items"],
            item["operation"],
            item["divisible_by"],
            item["test_true"],
            item["test_false"],
            worry_level_divider=3
        )
        for item in data
    ]

    for _ in range(20):
        for monkey in monkeys:
            for catching_monkey, worry_level in monkey.inspect_items():
                monkeys[catching_monkey].starting_items.append(worry_level)

    return (lambda x, y: x.items_inspected * y.items_inspected)(
        *sorted(monkeys, key=lambda monkey: monkey.items_inspected)[-2:]
    )


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
