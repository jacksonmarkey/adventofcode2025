# Laboratories

from collections import defaultdict

def main():
    with open("laboratories.txt") as file:
        first_line = file.readline().rstrip()
        tachyon_entrypoint = first_line.index('S')
        width = len(first_line)
        # maps column number to ordered list of that column's splitters' line numbers
        columnar_splitters = defaultdict(list)
        line_number = 1
        while line := file.readline().rstrip():
            for i, c in enumerate(line):
                if c == '^':
                    columnar_splitters[i].append(line_number)
            line_number += 1
        
        acc = 0
        seen = set()
        queue = [(tachyon_entrypoint, 0)]
        while len(queue) > 0:
            # for breaking from the outer for-loop below
            flag = False
            beam_col, beam_row = queue.pop()
            splitters = columnar_splitters[beam_col]
            for s in splitters:
                if s > beam_row:
                    for r in range(beam_row, s):
                        if (beam_col, r) in seen:
                            flag = True
                            break
                        seen.add((beam_col, r))
                    if flag:
                        break
                    acc += 1
                    left = (beam_col-1, s)
                    right = (beam_col+1, s)
                    if beam_col-1 >= 0 and left not in seen:
                        queue.append(left)
                    if beam_col+1 < width and right not in seen:
                        queue.append(right)
                    break
        print(acc)
            

if __name__=="__main__":
    main()