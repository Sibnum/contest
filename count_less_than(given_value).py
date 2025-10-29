nums = input()


def main(nums):
    nums = list(map(int, nums.split()))  # преобразовываем в список
    n = len(nums)  # считаем последний индекс массива
    result = []
    for index_1 in range(n):  # цикл по диапазону индексов
        count = 0
        index_2 = 0
        for index_2 in range(n):
            if nums[index_1] == nums[index_2]:
                continue
            if nums[index_1] > nums[index_2]:
                count += 1
        result.append(count)
    result = ' '.join(map(str, result))
    return result


if __name__ == '__main__':
    print(main(nums))
