# python_labs

## Лабораторная работа 1

### Задание 1
```python
name = input()
age = int(input())
print('Имя:' + name)
print('Возраст:' + str(age))
print("Привет," + name + "!", " Через год тебе будет " + str(age+1) + ".")
```
![Картинка 1](images/lab01/01.png)

### Задание 2
```python
a = input()
b = float(input())
print("a: " + a.replace('.', ','))
print("b: " + str(b))
print("sum=" + f"{(float(a)+b):.2f}" + ";" + " avg=" + f"{(float(a)+b)/2:.2f}")
```
![Картинка 2](./images/lab01/02.png)

### Задание 3
```python
price = int(input())
discount = int(input())
vat = int(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print("База после скидки: " + f"{base:.2f}" + " ₽")
print("НДС: " + f"{vat_amount:.2f}" + " ₽")
print("Итого к оплате: " + f"{total:.2f}" + " ₽")
```
![Картинка 3](./images/lab01/03.png)

### Задание 4
```python
m = int(input())
print('Минуты:' + ' ' + str(m))
print(str(m//60) + ":" + f"{(m%60):02d}")
```
![Картинка 4](./images/lab01/04.png)

### Задание 5
```python
Surname = str(input())
Name = str(input())
Otchestvo = str(input())
print("ФИО: ", Surname, Name, Otchestvo)
print("Инициалы: ", Surname[0] + Name[0] + Otchestvo[0] + '.')
print("Длина (символов): " + str(len(Surname) + len(Name) + len(Otchestvo) + 2))
```
![Картинка 5](./images/lab01/05.png)

### Задание 6
```python
form = []
tr = fl = 0
for n in range(int(input())):
    data = input().split()

    f = data[0] if len(data) > 0 else ""
    name = data[1] if len(data) > 1 else ""
    age = data[2] if len(data) > 2 else ""
    bol = data[3] if len(data) > 3 else ""

    form.append([f, name, age, bol])
for i in range(len(form)):
    print(str(i+1), form[i][0], form[i][1], form[i][2], form[i][3])
    if form[i][3] == 'True': tr += 1
    else: fl += 1
print("out:", tr, fl)
```
![Картинка 6](./images/lab01/06.png)

### Задание 7
```python
a = input()
print("in: " + a)
c = []
for i in range(len(a)):
    if a[i].isupper():
        cnt = i
        break
c.append(''.join([a[i] for i in range(cnt, len(a), 3)]))
print("out:", *c)
```
![Картинка 7](./images/lab01/07.png)




## Лабораторная работа 2

### Задание arrays.py
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        return tuple([min(nums), max(nums)])
    except ValueError:
        return 'ValueError'


print('----------min_max----------')
print(min_max([1, 2, 3, 4, 5]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    a = sorted(list(set(nums)))
    return a

print('----------unique_sorted----------')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    rlist = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                rlist.append(j)
        else:
            return 'TypeError'
    return rlist



print('----------flatten----------')
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![Картинка 1](images/lab02/01.png)

### Задание matrix.py
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    return [[mat[a][b] for a in range(len(mat))] for b in range(row_len)]


print('----------transpose----------')
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    return [sum(i) for i in mat]


print('----------row_sum----------')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    mat = transpose(mat)

    return [sum(i) for i in mat]


print('----------col_sums----------')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![Картинка 2](./images/lab02/02.png)

### Задание tuples.py
```python
def info(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio, str):
        raise TypeError("fio должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("group должно быть строкой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("gpa должно быть числом")

    return ((lambda x: f"{x[0].capitalize()} {x[1][0].upper()}.{'' + x[2][0].upper() + '.' if len(x) > 2 else ''}")(
        [a.capitalize() for a in fio.strip().split() if a]), group, f"{gpa:.2f}")


def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    inf = info(fio, group, gpa)
    answer = ''
    for _ in inf:
        answer += str(_) + ', '
    return answer[:-2]


print('----------format_record----------')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![Картинка 3](./images/lab02/03.png)

## Лабораторная работа 3

### Задание zadanie A.py
```python
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    while '   ' in text:
        text = text.replace('   ', ' ')
    return text.strip()


def tokenize(text: str) -> list[str]:
    text = text.replace('!', '')
    text = re.split(r'[^\w-]+', text)
    return text


def count_freq(tokens: list[str]) -> dict[str, int]:
    dic = {}
    unique = set(tokens)
    for _ in unique:
        dic[_] = tokens.count(_)
    return dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]


print('----------normalize----------')
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print('----------tokenize----------')
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print('----------count_freq + top_n----------')
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n({"a":3,"b":2,"c":1}, n=2))
print(top_n({"aa":2,"bb":2,"cc":1}, n=2))
```
![Картинка 1](images/lab03/01.png)

### Задание text_stats.py
```python
import sys
from src.lib import normalize, count_freq, top_n
text = input() # "Привет, мир! Привет!!!"
tokens = []
for word in normalize(text).split():
    clean_word = word.strip('.,!!!!?;:"()[]{}')
    if clean_word:
        tokens.append(clean_word)

total_words = len(tokens)
unique_words = len(count_freq(tokens))
top_words = top_n(count_freq(tokens), 5)
print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")
for word, count in top_words:
        print(f"{word}:{count}")
```
![Картинка 2](./images/lab03/02.png)

## Лабораторная работа 4

### Задание A.py
```python
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
```
![Картинка 1](images/lab04/01.png)

### Задание B.py
```python
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
```
![Картинка 2](./images/lab04/02.png)

## Лабораторная работа 5

### Задание A
```python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:# открываем JSON файл для чтения
            data = json.load(json_file)# кидаем все в data и преобразуем в питоновские объекты

        if not data or not isinstance(data, list):# проверяем на пустоту и список
            raise ValueError

        all_keys = set()#проходимся по всем элементас
        for item in data:#собираем все ключи словарей
            if not isinstance(item, dict):
                raise ValueError
            all_keys.update(item.keys())

        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=all_keys)# создаем writer понимающий структуру словарей
            writer.writeheader()
            for row in data:
                complete_row = {key: row.get(key, "") for key in all_keys}# для каждой строки создаем полный словарь
                writer.writerow(complete_row)

    except FileNotFoundError:
        raise FileNotFoundError


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:# открываем CSV файл для чтения
            reader = csv.DictReader(csv_file)# Читаем CSV как список словарей
            data = list(reader)# переделываем в списк
        if not data:
            raise ValueError

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)#записываем данные в JSON файл в красивом форматировании

    except FileNotFoundError:
        raise FileNotFoundError
```

### Задание B
```python
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        wb = Workbook()# создаем новую Excel кнгу
        ws = wb.active# получаем активный лист
        ws.title = "Sheet1"# переименовываем лист

        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)# создаем CSV reader
            for row in reader:# читаем острочно
                ws.append(row)# добавляем строку в Excel

        for column_cells in ws.columns:# проходим по каждому столбцу
            length = max(len(str(cell.value or "")) for cell in column_cells)#  находим макс длину текста в столбце
            ws.column_dimensions[column_cells[0].column_letter].width = max(length + 2, 8)# устанавливаем ширину

        wb.save(xlsx_path)# сохраняем Excel файл

    except FileNotFoundError:
        raise FileNotFoundError
```

### Задание test.py
```python
import sys
import os
from pathlib import Path

current_dir = Path(__file__).parents# получаем директорую файла
sys.path.insert(0, str(current_dir))# добавляем директорию в начало пути поиска

from src.lib import json_to_csv, csv_to_json, csv_to_xlsx
PROJECT_ROOT = Path(__file__).parent.parent.parent# поднимаемся на 3 уровня вверх от файла
json_source = PROJECT_ROOT / "data" / "samples" / "ex1.json"# берем и создаем в папке data
csv_source = PROJECT_ROOT / "data" / "samples" / "ex2.csv"
output_csv = PROJECT_ROOT / "data" / "out" / "ex1.csv"
output_json = PROJECT_ROOT / "data" / "out" / "ex2.json"
output_xlsx = PROJECT_ROOT / "data" / "out" / "ex3.xlsx"
try:
    json_to_csv(str(json_source), str(output_csv))# преобразуем в нужные форматы
    csv_to_json(str(csv_source), str(output_json))
    csv_to_xlsx(str(csv_source), str(output_xlsx))
except Exception as x:# сохраняем ошибку в переменную х и выводим
    print(f"Ошибка: {x}")
```
![Картинка 3](./images/lab02/03.png)
