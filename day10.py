from itertools import combinations

def minimum_presses(target_pattern: list[bool], buttons: list[list[bool]]) -> int:
    n_lights = len(target_pattern)
    for subset_size in range(len(buttons)):
        for subset in combinations(buttons, subset_size):
            result = [False] * n_lights
            for button in subset:
                for i in range(n_lights):
                    result[i] = (result[i] != button[i])
            if result == target_pattern:
                return subset_size
                    
def main():
    sum = 0
    with open("factory.txt") as file:
        while line := file.readline():
            line = line.split(' ')
            indicator_lights = []
            buttons = []
            for i, s in enumerate(line):
                if i == 0:
                    indicator_lights = [c == '#' for c in s[1:-1]]
                elif i < len(line)-1:
                    b = s[1:-1].split(',')
                    buttons.append([str(n) in b for n in range(len(indicator_lights))])
            # print(indicator_lights)
            # print(buttons)
            sum += minimum_presses(indicator_lights, buttons)
    print(sum)  

if __name__=="__main__":
    main()