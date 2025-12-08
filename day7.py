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
    
    # part 1
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

    # part 2
    def find_target(beam_col, beam_row):
        splitters = columnar_splitters[beam_col]
        for s in splitters:
            if s > beam_row:
                return (beam_col, s)
        return (beam_col, -1)

    multiplicity = dict()
    def split(beam_col, beam_row) -> int:
        left = (beam_col-1, beam_row)
        right = (beam_col+1, beam_row)
        m = 0
        if beam_col-1 >= 0:
            left_target = find_target(left[0], left[1])
            if left_target[1] == -1:
                m += 1
            elif left_target in multiplicity:
                m += multiplicity[left_target]
            else:
                m += split(left_target[0], left_target[1])
        if beam_col+1 < width:
            right_target = find_target(right[0], right[1])
            if right_target[1] == -1:
                m += 1
            elif right_target in multiplicity:
                m += multiplicity[right_target]
            else:
                m += split(right_target[0], right_target[1])
        multiplicity[(beam_col, beam_row)] = m
        return m
    
    timelines = 0
    emitter_target = find_target(tachyon_entrypoint, 0)
    if emitter_target == -1:
        timelines = 1
    else:
        timelines = split(emitter_target[0], emitter_target[1])
    print(timelines)
        


if __name__=="__main__":
    main()