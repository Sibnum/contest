def decoding(command: str) -> str:
    stack: list = []
    current_string: str = ''
    current_number: str = ''
    for symbol in command:
        if symbol.isdigit():
            current_number += symbol
        elif symbol.isalpha():
            current_string += symbol
        elif symbol == '[':
            stack.append(int(current_number))
            stack.append(current_string)
            current_number: str = ''
            current_string: str = ''
        elif symbol == ']':
            previous_string: str = stack.pop()
            repeat_number: int = stack.pop()
            current_string = previous_string + current_string * repeat_number
    return current_string


if __name__ == '__main__':
    command: str = input()
    print(decoding(command))
