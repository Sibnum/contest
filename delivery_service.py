# ID 147023292
"""Служба доставки (Delivery service).

Программа определяем минимальное количество транспортных платформ для
перевозки роботов. Для определения количества платформ используется метод
двух указателей.

Основные компоненты:

**weights_of_robots** - ввод отдельных весов роботов, указанных через пробел.
Вес роботов не может превышать грузоподъёмность платформы.

**limit** - ввод предельной грузоподъёмности платформы. На платформе может
находится не более 2 роботов одновременно.

**platform_count_calculation** - функция, определяющая количество платформ для
перевозки роботов.
"""

weights_of_robots: str = input()
limit: int = int(input())


def platform_count_calculation(weights_of_robots: str, limit: int) -> int:
    """Определяет количество платформ необходимых для перевозки роботов.

    Возвращает целое число - количество платформ.
    """
    weight: list[int] = list(map(int, weights_of_robots.split()))
    sorted_weights: list[int] = sorted(weight)
    left_index: int = 0
    right_index: int = len(sorted_weights) - 1
    platforms: int = 0
    while left_index <= right_index:
        if sorted_weights[left_index] + sorted_weights[right_index] <= limit:
            platforms += 1
            left_index += 1
            right_index -= 1
        else:
            platforms += 1
            right_index -= 1
    return platforms


if __name__ == '__main__':
    print(platform_count_calculation(weights_of_robots, limit))
