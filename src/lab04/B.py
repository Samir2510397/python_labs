from pathlib import Path
from src.lib import tokenize, normalize, top_n, count_freq
from io_txt_csv import read_text, write_csv

current_file = Path(__file__)#создаем обьект path являющийся текущим файлом
input_path = current_file.parent.parent / "src/data/input_test.txt"#строим путь в родительскую директорию и добавляем туда относительный путь
output_path = current_file.parent.parent / "src/data/output.csv"

print(f"Текущий файл: {current_file}")
print(f"Входной файл: {input_path}")
print(f"Выходной файл: {output_path}")

input_path.parent.mkdir(parents=True, exist_ok=True)#создаем директорию для входного файла  если она не существует
if input_path.exists():#проверяем существует ли файл по указанному пути
    input_path.unlink()
input_path.write_text("Привет", encoding="utf-8")#создаем новый файл и записываем туда текст
print(f"Создан пустой файл: {input_path}")

text = read_text(input_path, "utf-8")#читаем файл
print(f"Прочитано: '{text}' ({len(text)} символов)")

normalized_text = normalize(text)#колдуем нашими функциями
tokens = tokenize(normalized_text)
frequencies = count_freq(tokens)

print(f"Токены: {tokens}")
print(f"Частоты: {frequencies}")

word_counts = top_n(frequencies, n=len(frequencies))#получаем отсортированные по частоте слова
write_csv([[word, count] for word, count in word_counts],#подготавливаем слова для записи
          output_path, header=('word', 'count'))#вызываем функцию записи
print(f"CSV создан: {output_path}")

print(f"Всего слов: {sum(frequencies.values())}")
print(f"Уникальных слов: {len(frequencies)}")

print("Топ 5 слов:")
top_5 = top_n(frequencies, n=5)
for i, (word, count) in enumerate(top_5, 1):
    print(f"  {i}. '{word}': {count}") if top_5 else print("  Нет слов")