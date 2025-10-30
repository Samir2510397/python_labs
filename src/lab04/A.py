from pathlib import Path
import sys

current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from src.lib import tokenize, normalize, top_n, count_freq
from io_txt_csv import read_text, write_csv

def main():
    current_file = Path(__file__)
    print(f"Текущий файл: {current_file}")

    input_path = current_file.parent / 'data' / 'input.txt'
    output_path = current_file.parent / 'data' / 'output.csv'

    print(f"Путь к входному файлу: {input_path}")
    print(f"Путь к выходному файлу: {output_path}")

    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text("Привет, мир! Привет!!!", encoding='utf-8')
    print(f"Создан/обновлен файл: {input_path}")

    result = read_text(input_path)
    print(f"Результат чтения: {result}")

    normalized_text = normalize(result)
    print(f"Нормализованный текст: {normalized_text}")

    tokens = tokenize(normalized_text)
    print(f"Токены: {tokens}")

    frequencies = count_freq(tokens)
    print(f"Частоты: {frequencies}")

    word_counts = top_n(frequencies, n=len(frequencies))
    print(f"Подсчет слов: {word_counts}")

    write_csv(word_counts, output_path, header=('word', 'count'))
    print(f"CSV файл создан: {output_path}")

if __name__ == "__main__":
    main()