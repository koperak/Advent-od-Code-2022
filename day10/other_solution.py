def read_input(path: str = 'testinput.txt'):
    inputs = []
    with open(path) as filet:
        for line in filet.readlines():
            line = line.rstrip()
            line = line.split(' ')
            if len(line) == 1:
                inputs.append([line[0], 0])
            else:
                inputs.append(['noop', 0])
                inputs.append([line[0], int(line[1])])
    return inputs


def main1():
    result = 0

    # get the inputs
    inputs = read_input()
    print(inputs)
    # go through the inputs
    x_register = 1
    for cycle, (instruction, value) in enumerate(inputs, 1):

        # make the cycle check
        if (cycle + 20) % 40 == 0:
            result += x_register*cycle

        # update the signal
        x_register += value

    print(f'The result for solution 1 is: {result}')

main1()