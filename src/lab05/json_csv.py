import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:# открываем JSON файл для чтения
            data = json.load(json_file)# кидаем все в data и преобразуем в питоновские объекты

        if not data or not isinstance(data, list):# проверяем на пустоту и список
            raise ValueError

        all_keys = set()#set для избежания дубликатов
        for item in data:# проходим по всем элементам списка и собираем все ключи словарей
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
            json.dump(data, json_file, ensure_ascii=False, indent=2)#записываем данные в JSON файл в красивом форматировании и кириллицей

    except FileNotFoundError:
        raise FileNotFoundError