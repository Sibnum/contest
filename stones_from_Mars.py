def main(n: int, weights_n: list[int], m: int, weights_m: list[int]) -> int:
    weights_n.sort()
    weights_m.sort()
    m_index: int = 0
    result: int = 0
    for i_n in range(n):
        for i_m in range(m_index, m):
            if i_n > i_m:
                return result
            if weights_m[i_m] >= weights_n[i_n]:
                result += 1
                m_index = i_m + 1
                break
            else:
                continue
    return result


if __name__ == '__main__':
    n: int = int(input())
    weights_n_str: str = input()
    m: int = int(input())
    weights_m_str: str = input()
    weights_n: list[int] = [int(digit) for digit in weights_n_str.split()]
    weights_m: list[int] = [int(digit) for digit in weights_m_str.split()]
    print(main(n, weights_n, m, weights_m))
