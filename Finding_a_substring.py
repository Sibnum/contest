string = input()


def main(string: str) -> int:
    left = 0
    max_length = 0
    char_index: dict = {}
    for right in range(len(string)):
        current_char = string[right]
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1
        char_index[current_char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    return max_length


if __name__ == '__main__':
    print(main(string))
