def main():
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




if __name__=="__main__":
    main()