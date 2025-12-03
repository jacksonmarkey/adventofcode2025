# Lobby

def max_joltage_double_digit(bank: str) -> int:
    assert len(bank) >= 2
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

def max_joltage_n_digit(bank: str, on: int) -> int:
    assert len(bank) >= on
    output = ""
    for d in range(on):
        max = int(bank[0])
        max_idx = 0
        for idx in range(1, len(bank) - on + d + 1):
            n = int(bank[idx])
            if n > max:
                max = n
                max_idx = idx
        output += bank[max_idx]
        bank = bank[max_idx+1:]
    return int(output)


def main():
    double_digit_total = 0
    n_digit_total = 0
    with open("lobby.txt") as file:
        for bank in file:
            double_digit_total += max_joltage_double_digit(bank.rstrip())
            n_digit_total += max_joltage_n_digit(bank.rstrip(), 12)
    print(double_digit_total)
    print(n_digit_total)


if __name__=="__main__":
    main()