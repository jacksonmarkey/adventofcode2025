from collections import defaultdict
import matplotlib.pyplot as plt

def visualize(data):
    # exploratory plotting of our data
    data.append(data[0]) #repeat the first point to create a 'closed loop'

    xs, ys = zip(*data) #create lists of x and y values

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()
    
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

    visualize(tiles)

    # part 2
    # stupid ass solution
    upper_corner = [94987,50332]
    lower_corner = [94987,48421]
    corner_x = 94987
    ymax = 65738
    ymin = 33493
    # for i in range(n_tiles-1):
    #     if tiles[i] == upper_corner or tiles[i] == lower_corner or tiles[i+1] == upper_corner or tiles[i+1] == lower_corner:
    #         continue
    #     if tiles[i][0] <= corner_x <= tiles[i+1][0]:
    #         print(f"{tiles[i]}<->{tiles[i+1]}")        
    #     if tiles[i+1][0] <= corner_x <= tiles[i][0]:
    #         print(f"{tiles[i]}<->{tiles[i+1]}")        

    max_area = 0
    answer = []
    for i in range(n_tiles):
        x1, y1 = tiles[i]
        if ymax >= y1 > upper_corner[1]:
            x2, y2 = upper_corner
        elif ymin <= y1 < lower_corner[1]:
            x2, y2 = lower_corner
        else:
            continue
        length = abs(x2-x1) + 1
        height = abs(y2-y1) + 1
        area = length * height
        if area > max_area:
            answer = [x1, y1]
            max_area = area
    print(max_area)


if __name__=="__main__":
    main()