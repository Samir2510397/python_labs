from pathlib import Path
import sys

current_dir = Path(__file__).parent# получаем директорию текущего файла
sys.path.append(str(current_dir))# Добавляем эту директорию в путь поиска модулей

from src.lib import tokenize, normalize, top_n, count_freq
from io_txt_csv import read_text, write_csv

def main():
    current_file = Path(__file__)# получаем путь к исполняемому файлу
    print(f"Текущий файл: {current_file}")# кои выводим его

    input_path = current_file.parent / 'data' / 'input.txt'# путь к входному
    output_path = current_file.parent / 'data' / 'output.csv'# путь у выходному

    print(f"Путь к входному файлу: {input_path}")
    print(f"Путь к выходному файлу: {output_path}")
    # создаем директорию и тестовый файл
    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text("Привет, мир! Привет!!!", encoding='utf-8')#записываем туда текст
    print(f"Создан/обновлен файл: {input_path}")

    result = read_text(input_path)#читаем текст из файла
    print(f"Результат чтения: {result}")

    normalized_text = normalize(result)#нормализуем его
    print(f"Нормализованный текст: {normalized_text}")

    tokens = tokenize(normalized_text)#разбиваем его
    print(f"Токены: {tokens}")

    frequencies = count_freq(tokens)#считаем частоты
    print(f"Частоты: {frequencies}")

    word_counts = top_n(frequencies, n=len(frequencies))#сортируем частоты по частоте
    print(f"Подсчет слов: {word_counts}")

    write_csv(word_counts, output_path, header=('word', 'count'))#записываем в csv
    print(f"CSV файл создан: {output_path}")

if __name__ == "__main__":
    main()# Запускаем основную функцию при прямом выполнении файла