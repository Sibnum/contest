first_str = input()
second_str = input()


def main(second_str):
    second_str = second_str.split()
    digit = []
    spaces = []
    for symbol in second_str:
        if symbol not in digit:
            digit.append(symbol)
        else:
            symbol = '_'
            spaces.append(symbol)
    digit.extend(spaces)
    result = ' '.join(digit)
    return result


if __name__ == '__main__':
    result = main(second_str)
    print(result)
