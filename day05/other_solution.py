from copy import deepcopy
from itertools import zip_longest
import re

with open(__file__.replace(".py", "_data")) as f:
    drawing, instructions = [x.split("\n") for x in f.read().split("\n\n")]

# INPUT PARSING
crates = [
    "".join(col[-2::-1]).strip()
    for idx, col in enumerate(zip_longest(*drawing, fillvalue=""))
    if idx % 4 == 1
]
moves = [map(int, re.findall(r"\d+", line)) for line in instructions]

# PART 1 & 2
pos9000, pos9001 = [deepcopy(crates) for _ in [1, 2]]
for num, initial, final in moves:
    pos9000[final - 1] += pos9000[initial - 1][: -num - 1 : -1]
    pos9000[initial - 1] = pos9000[initial - 1][:-num]

    pos9001[final - 1] += pos9001[initial - 1][-num:]
    pos9001[initial - 1] = pos9001[initial - 1][:-num]

print("".join(x[-1] for x in pos9000) + "\n" + "".join(x[-1] for x in pos9001))
