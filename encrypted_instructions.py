# ID149375970
"""Шифрованные инструкции (Encrypted_instructions).

Программа расшифровывает сжатые сообщения и возвращает строку с командами.

Основные компоненты:

**command** - ввод сокращённой формы команды. В строке могут быть только числа,
буквы и квадратные скобки.

**decoding** - функция, декодирующая сокращённую форму команды в полную форму.
"""

import string


def decoding(command: str) -> str:
    """Декодирует сокращённую форму команды в полную форму.

    На вход принимает строку с сокращённой формой команды. Алгоритм
    декодирования использует стэк.
    Возвращает строку с полной формой команды.
    """
    stack: list[tuple[str, str]] = []
    current_string: str = ''
    current_number: str = ''
    for symbol in command:
        if symbol in set(string.digits):
            current_number += symbol
        elif symbol == '[':
            stack.append((current_string, current_number))
            current_string = ''
            current_number = ''
        elif symbol == ']':
            previous_string, repeat_number = stack.pop()
            current_string = (
                previous_string + current_string * int(repeat_number)
                )
        else:
            current_string += symbol
    return current_string


if __name__ == '__main__':
    command: str = input()
    print(decoding(command))
