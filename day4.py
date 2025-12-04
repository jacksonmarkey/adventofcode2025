# Printing Department

ROLL = '@'

def neighbor_indices(ylen: int, xlen: int, i: int, j: int) -> list[(int, int)]:
    ret = []
    deltas = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    for dy, dx in deltas:
        if 0 <= i+dy < ylen and 0 <= j+dx < xlen :
            ret.append((i+dy, j+dx))
    return ret        

def rolls_adjacent(input: list[list[str]], y: int, x: int) -> int:
    acc = 0
    neighbors = neighbor_indices(len(input), len(input[0]), y, x)
    for i, j in neighbors:
        if input[i][j] == ROLL:
            acc += 1
    return acc

def accessible_rolls(input: list[list[str]]) -> list[(int, int)]:
    acc = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == ROLL and rolls_adjacent(input, y, x) < 4:
                acc.append((y, x))
    return acc


def main():
    with open("printing.txt") as file:
        # part 1
        input = [list(l.rstrip()) for l in file.readlines()]
        accessible = accessible_rolls(input)
        print(len(accessible))
        # part 2
        removed = 0
        while True:
            removed += len(accessible)
            for y, x in accessible:
                input[y][x] = 'x'
            new_accessible = accessible_rolls(input)
            if len(new_accessible) == 0:
                break
            accessible = new_accessible
        print(removed)
        




if __name__=="__main__":
    main()