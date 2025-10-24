example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    last_index = len(data) - 1
    item_index = 0
    swapped = False
    while last_index != 1 or swapped is True:
        for i in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
                item_index += 1
            if swapped is True:
                last_index -= 1
                continue
            else:
                swapped is False
                break
    return data


print(bubble_sort(example_array))
