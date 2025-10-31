from pathlib import Path
import csv
import re

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла"""
    print(f"Читаю файл: {path}")# какой файл читаем
    p = Path(path) # Создаем объект Path из переданного пути
    text = p.read_text(encoding=encoding)# Читаем текст с указанной кодировкой
    print(f"Прочитал {len(text)} символов")# кол-во прочитанных слов
    return text# возращаем прочитанный текст


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV файл"""
    p = Path(path)# Создаем объект Path для выходного файла
    # проверка
    if rows:# если есть строки для записи
        first_length = len(rows[0])# запоминаем длину первой строки
        for i, row in enumerate(rows):# перебираем все строки и их индексы
            if len(row) != first_length:# если длина не совпадает с первой
                raise ValueError(f"ошибка лютая")# возвращаем ошибку
    # записываем файл
    with p.open('w', newline='', encoding='utf-8') as f:# открываем файл
        writer = csv.writer(f)# создаем обьект для csv

        if header is not None:# если передан заголовок
            writer.writerow(header)# то записываем строку заголовка

        for row in rows:# перебираем все строки
            writer.writerow(row)# записываем каждую строку в csv

