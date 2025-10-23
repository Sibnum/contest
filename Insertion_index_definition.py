first_str = input()
second_str = input()


def main(first_str, second_str):
    first_str = first_str.split()
    first_str = [int(digit) for digit in first_str]
    second_str = int(second_str)
    left_index = 0
    right_index = len(first_str) - 1
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        if first_str[mid_index] == second_str:
            if first_str[0] == second_str:
                return 0
            else:
                return mid_index
        if first_str[mid_index] < second_str:
            left_index = mid_index + 1
        else:
            right_index = mid_index
    if left_index == right_index:
        for index in range(len(first_str)):
            if first_str[index] < second_str:
                continue
            elif first_str[index] > second_str:
                return index
        return index + 1


if __name__ == '__main__':
    result = main(first_str, second_str)
    print(result)
