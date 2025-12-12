def main():
    counter = 50
    acc = 0
    with open("secret.txt") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            print(f"{direction}{distance}")
            if direction == "L":
                counter -= distance
            else:
                counter += distance
            if counter % 100 == 0:
                acc += 1
    print(acc)


if __name__=="__main__":
    main()