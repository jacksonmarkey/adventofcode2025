# Cafeteria


def main():
    with open("cafeteria.txt") as file:
        # part 1
        fresh = []
        while line := file.readline().rstrip():
            a, b = line.split("-")
            fresh.append((int(a),int(b)))
        fresh_count = 0
        while line := file.readline().rstrip():
            i = int(line)
            for a, b in fresh:
                if a <= i <= b:
                    fresh_count += 1
                    # print(f"{i}-<[{a},{b}]")
                    break
        print(fresh_count)
        




if __name__=="__main__":
    main()