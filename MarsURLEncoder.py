"""Модуль для шифрования и дешиврования ссылок."""

import random


class MarsURLEncoder:
    """Класс для шифровки и расшифровки ссылок."""

    def __init__(self) -> None:
        """Инициализирует словарь с ссылками, в котором ключ — это
    сгенерированная зашифрованная ссылка, значение — исходная ссылка.
    """
        self.link_repository = {}
        self.symbol_for_hash = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

    def encode(self, long_url: str) -> str:
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol.
        И проверяет ключ на коллизию.
        """
        self.long_url = long_url
        hash = ''.join(random.choice(self.symbol_for_hash) for i in range(6))
        while hash in self.link_repository.keys():
            hash = (
                ''.join(random.choice(self.symbol_for_hash) for i in range(6))
            )
        short_url = f'https://ma.rs/{hash}'
        self.link_repository[short_url] = self.long_url
        return short_url

    def decode(self, short_url: str) -> str:
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        self.short_url = short_url
        long_url = self.link_repository[short_url]
        return long_url
