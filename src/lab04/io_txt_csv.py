from pathlib import Path
import csv
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: приводит к нижнему регистру, заменяет ё на е, убирает лишние пробелы"""
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    text = text.strip()
    return text


def tokenize(text: str) -> list[str]:
    """Разбивает текст на токены (слова)"""
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту каждого токена"""
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N самых частых токенов"""
    items = []
    for word in freq:
        count = freq[word]
        items.append((word, count))
    items.sort(key=lambda i: (-i[1], i[0]))
    return items[:n]


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла"""
    print(f"Читаю файл: {path}")
    p = Path(path)
    text = p.read_text(encoding=encoding)
    print(f"Прочитал {len(text)} символов")
    return text


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV файл"""
    p = Path(path)

    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"ошибка лютая")

    with p.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)