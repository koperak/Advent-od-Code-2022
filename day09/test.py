TESTDATA = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

def parse(raw_data):
    return [x.split(' ') for x in raw_data.split('\n')]

# instructions for heads motions 
mot = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

# starting poin 's' for Heads and Tails
hx, hy = 0, 0
tx, ty = 0, 0

