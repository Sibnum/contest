def main(n: int, m: int, array_n: list[int], array_m: list[int]) -> str:
    result = []
    for i_m in range(m):
        current_m = array_m[i_m]
        for i_n in range(n):
            current_n = array_n[i_n]
            if current_n == current_m:
                result.append(current_n)
    last_digit = []
    for i_n in range(n):
        current_n = array_n[i_n]
        found = False
        for i_m in range(m):
            current_m = array_m[i_m]
            if current_n == current_m:
                found = True
                break
        if not found:
            last_digit.append(current_n)
    last_digit.sort()
    result.extend(last_digit)
    return ' '.join([str(i) for i in result])


if __name__ == '__main__':
    n: int = int(input())
    array_n_str: str = input()
    m: int = int(input())
    array_m_str: str = input()
    array_n: list = [int(digit) for digit in array_n_str.split()]
    array_m: list = [int(digit) for digit in array_m_str.split()]
    print(main(n, m, array_n, array_m))
