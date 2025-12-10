def part_1():
    lines = []
    with open("trash.txt") as file:
        while line := file.readline():
            lines.append(line.split())
    operands = lines[-1]
    n_ops = len(operands)
    acc = [0 if o == "+" else 1 for o in operands]
    for l in lines[:-1]:
        for i in range(n_ops):
            if operands[i] == "+":
                acc[i] += int(l[i])
            else:
                acc[i] *= int(l[i])
    print(sum(acc))

def part_2():
    with open("trash.txt") as file:
        [l1, l2, l3, l4, l5] = file.read().splitlines()
        n_cols = len(l1)
        acc = 0
        operand = ''
        nums = []
        for c in range(n_cols):
            c1, c2, c3, c4, c5 = l1[c], l2[c], l3[c], l4[c], l5[c]
            if (c1,c2,c3,c4,c5) == (' ',' ',' ',' ',' '):
                if operand == '+':
                    acc += sum(nums)
                else:
                    product = 1
                    for n in nums:
                        product *= n
                    acc += product
                nums = []
                continue
            if c5 != ' ':
                operand = c5
            nums.append(int(c1+c2+c3+c4))
        # last column logic
        if operand == '+':
            acc += sum(nums)
        else:
            product = 1
            for n in nums:
                product *= n
            acc += product
        print(acc)


def main():
    part_1()
    part_2()




if __name__=="__main__":
    main()