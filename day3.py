# Lobby

def max_joltage(bank) -> int:
    assert len(bank) > 2
    max = int(bank[0])
    max_idx = 0
    for idx in range(1, len(bank)-1):
        digit = int(bank[idx])
        if digit > max:
            max = int(digit)
            max_idx = idx
    submax = int(bank[max_idx+1])
    for idx in range(max_idx+2, len(bank)):
        digit = int(bank[idx])
        if digit > submax:
            submax = digit
    return int(str(max) + str(submax))

def main():
    total = 0
    with open("lobby.txt") as file:
        for bank in file:
            total += max_joltage(bank.rstrip())
    print(total)


if __name__=="__main__":
    main()