def main(n: int, m: int, array_n: list[int], array_m: list[int]) -> str:
    result = []
    last_digit = []
    for i_m in range(m):  # итерируем по кол-ву цифр
        current_m = array_m[i_m]
        for i_n in range(n):
            current_n = array_n[i_n]
            if current_n == current_m:
                result.append(current_n)
        if current_n != current_m:  # переписать на цикл с индекса array_m + 1
            last_digit.append(current_n)
    last_digit.sort()
    result.extend(last_digit)
    return ' '.join([str(i) for i in result])


if __name__ == '__main__':
    n: int = int(input())  # кол-во чисел, которые надо отсортировать
    array_n: str = input()  # строка с n чисел, которые надо отсортировать
    m: int = int(input())  # кол-во чисел в шаблоне
    array_m: str = input()  #строка с m чисел - шаблон
    array_n: list = [int(digit) for digit in array_n.split()]  #список для сорт
    array_m: list = [int(digit) for digit in array_m.split()]  #список-шаблон
    print(main(n, m, array_n, array_m))
