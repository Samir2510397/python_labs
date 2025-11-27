import re
import csv
import json
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        return (min(nums), max(nums))
    except ValueError:
        return 'ValueError'


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    a = sorted(list(set(nums)))
    return a


def flatten(mat: list[list | tuple]) -> list:
    rlist = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                rlist.append(j)
        else:
            return 'TypeError'
    return rlist


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    while '   ' in text:
        text = text.replace('  ', '')
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
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]


def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    return [[mat[a][b] for a in range(len(mat))] for b in range(row_len)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    return [sum(i) for i in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'

    mat = transpose(mat)

    return [sum(i) for i in mat]


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


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        if not data or not isinstance(data, list):
            raise ValueError

        all_keys = set()
        for item in data:
            if not isinstance(item, dict):
                raise ValueError
            all_keys.update(item.keys())

        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=all_keys)  # записывает список словарей
            writer.writeheader()
            for row in data:
                complete_row = {key: row.get(key, "") for key in all_keys}
                writer.writerow(complete_row)

    except FileNotFoundError:
        raise FileNotFoundError


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        if not data:
            raise ValueError

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    except FileNotFoundError:
        raise FileNotFoundError


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        wb = Workbook()  # создаем файл в экселе
        ws = wb.active  # создаем активный лист в экселе
        ws.title = "Sheet1"

        # Читаем CSV и записываем в XLSX
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ws.append(row)

        # Настраиваем авто-ширину колонок
        for column_cells in ws.columns:
            length = max(len(str(cell.value or "")) for cell in
                         column_cells)  # находим самую длинную строку в колонке для ориентира
            ws.column_dimensions[column_cells[0].column_letter].width = max(length + 2,
                                                                            8)  # column_dimensions - определяет букву столбца, width - присваивает ему ширину (минимум 8, +2 - запасные знаки на пробелы с двух сторон)

        wb.save(xlsx_path)

    except FileNotFoundError:
        raise FileNotFoundError