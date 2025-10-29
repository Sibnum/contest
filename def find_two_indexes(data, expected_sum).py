def find_two_indexes(data, expected_sum):
    for first_index in range(len(data) - 1):
        for second_index in range(len(data) - 1):
            if first_index == second_index:
                continue
            if data[first_index] + data[second_index] == expected_sum:
                return first_index, second_index


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
