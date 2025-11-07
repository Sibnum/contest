# ID 147834521
"""Шифрованные инструкции (Encrypted_instructions).

Программа расшифровывает сжатые сообщения и возвращает строку с командами.

Основные компоненты:

**command** - ввод сокращённой формы команды. В строке могут быть только числа,
буквы и квадратные скобки.

**decoding** - функция, декодирующая сокращённую форму команды в полную форму.
"""


def decoding(command: str) -> str:
    """Декодирует сокращённую форму команды в полную форму.

    На вход принимает строку с сокращённой формой команды. Алгоритм
    декодирования использует стэк.
    Возвращает строку с полной формой команды.
    """
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
            current_number = ''
            current_string = ''
        elif symbol == ']':
            previous_string: str = stack.pop()
            repeat_number: int = stack.pop()
            current_string = previous_string + current_string * repeat_number
    return current_string


if __name__ == '__main__':
    command: str = input()
    print(decoding(command))
