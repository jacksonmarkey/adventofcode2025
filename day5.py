# Cafeteria

def insert_sorted(fresh: list[tuple[int, int]], a: int, b: int) -> list[tuple[int, int]]:
    for n in range(len(fresh)):
        x, _ = fresh[n]
        if x > a:
            fresh.insert(n, (a, b))
            return fresh
    fresh.append((a, b))
    return fresh

def merge_intervals(l: list[tuple[int, int]]) -> list[tuple[int, int]]:
    acc = []
    # last merged interval
    x, y = l[0]
    for a, b in l[1:]:
        if a <= y + 1:
            y = max(b, y)
        else:
            acc.append((x, y))
            x, y = a, b
    acc.append((x, y))
    return acc


def main():
    with open("cafeteria.txt") as file:
        fresh = []
        while line := file.readline().rstrip():
            a, b = line.split("-")
            fresh = insert_sorted(fresh, int(a), int(b))
        fresh = merge_intervals(fresh)

        # part a
        fresh_inventory = 0
        while line := file.readline().rstrip():
            i = int(line)
            for a, b in fresh:
                if a <= i <= b:
                    fresh_inventory += 1
                    # print(f"{i}-<[{a},{b}]")
                    break
        print(fresh_inventory)

        # part b
        fresh_id_count = 0
        for a, b in fresh:
            fresh_id_count += (b-a+1)
        print(fresh_id_count)
        




if __name__=="__main__":
    main()