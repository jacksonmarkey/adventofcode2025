import heapq
from math import sqrt

def distance_sqrd(coord1, coord2) -> int:
    return (coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2 + (coord1[2]-coord2[2])**2

def main():
    boxes = []
    with open("playground.txt") as file:
        while line := file.readline().rstrip():
            coords = line.split(',')
            boxes.append([int(n) for n in coords])
    
    lines = []
    for b1 in range(len(boxes)):
        for b2 in range(b1+1, len(boxes)):
            d = distance_sqrd(boxes[b1], boxes[b2])
            heapq.heappush(lines, (d, b1, b2))

    circuits = dict[int, list]()
    def merge(b1, b2):
        if b1 not in circuits and b2 not in circuits:
            c = [b1, b2]
            circuits[b1] = c
            circuits[b2] = c
        elif b1 not in circuits:
            c2 = circuits[b2]
            c2.append(b1)
            for b in c2:
                circuits[b] = c2
        elif b2 not in circuits:
            c1 = circuits[b1]
            c1.append(b2)
            for b in c1:
                circuits[b] = c1
        else:
            c1 = circuits[b1]
            c2 = circuits[b2]
            if c1 == c2:
                return
            c_merged = c1 + c2
            for b in c_merged:
                circuits[b] = c_merged

    # part 1
    for i in range(1000):
        _, b1, b2 = heapq.heappop(lines)
        merge(b1, b2)

    # largest circuits
    c1, c2, c3 = [], [], []
    for c in circuits.values():
        if c in [c1, c2 ,c3]:
            continue
        if len(c) > len(c1):
            c1, c2, c3 = c, c1, c2
            continue
        if len(c) > len(c2):
            c2, c3 = c, c2
            continue
        if len(c) > len(c3):
            c3 = c
    print(len(c1) * len(c2) * len(c3))

    # part 2
    num_boxes = len(boxes)
    while True:
        _, b1, b2 = heapq.heappop(lines)
        merge(b1, b2)
        if len(circuits[0]) == num_boxes:
            b1x = boxes[b1][0]
            b2x = boxes[b2][0]
            print(b1x * b2x)
            return

if __name__=="__main__":
    main()