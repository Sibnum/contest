def calc(digit_n: int, digit_k: int) -> int:
    if digit_n == 1:
        return 0
    return (calc(digit_n - 1, digit_k) + digit_k) % digit_n


if __name__ == '__main__':
    digit_n: int = int(input())
    digit_k: int = int(input())
    print(calc(digit_n, digit_k) + 1)
