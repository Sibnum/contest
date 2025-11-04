def main(digits: list) -> int:
    max_digit = 0
    blocks = 0
    for i in range(len(digits)):
        if digits[i] > max_digit:
            max_digit = digits[i]
        if max_digit == i:
            blocks += 1
    return blocks


if __name__ == '__main__':
    n: int = int(input())
    m: str = input()
    digits = [int(i) for i in m.split()]
    print(main(digits))
