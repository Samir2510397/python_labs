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