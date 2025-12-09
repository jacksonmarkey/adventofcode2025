def main():
    tiles = []
    with open("movie.txt") as file:
        while line := file.readline().rstrip():
            tiles.append([int(s) for s in line.split(',')])

    # part 1
    max_area = 0
    n_tiles = len(tiles)
    for i in range(n_tiles):
        for j in range(i+1, n_tiles):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            length = abs(x2-x1) + 1
            height = abs(y2-y1) + 1
            area = length * height
            if area > max_area:
                max_area = area
    print(max_area)


if __name__=="__main__":
    main()