import pytest
import json, csv
from pathlib import Path
from src.lib import json_to_csv, csv_to_json


##Позитивный сценарий: конвертация JSON → CSV, все совпадает
def test_json_to_csv(tmp_path: Path):
    src = tmp_path / "people.json" #Создаем временные файлы через tmp_path (автоочистка после теста)
    dst = tmp_path / "people.csv"
    json_data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2 #Количество записей (2 строки)
    assert {"name", "age"} <= set(rows[0].keys()) #Наличие нужных колонок (name, age)


##Негативный сценарий: пустой входной файл → ValueError
def test_json_to_csv_empty(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    empty_json_data = []
    src.write_text(json.dumps(empty_json_data), encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


##Негативный сценари: JSON не список (некорректно записан) → ValueError
def test_json_to_csv_invalid(tmp_path: Path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "out.csv"
    invalid_json_data = '{"name": "Alice", "age": 22'
    src.write_text(json.dumps(invalid_json_data), encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


##Позитивный сценарий: конвертация CSV → JSON, все совпадает
def test_csv_to_json(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    csv_data = """name,age
Alice,22
Bob,25"""

    src.write_text(csv_data, encoding = "utf-8")
    csv_to_json(str(src), str(dst))

    with dst.open(encoding = "utf-8") as f:
        result_data = json.load(f)

    assert isinstance(result_data, list) and len(result_data) == 2 #Результат - список, 2 элемента в списке
    assert set(result_data[0]) == {"name", "age"} # Правильные ключи в объектах


##Негативный сценарий: несуществующий путь к файлу → FileNotFoundError
def test_file_error(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")  # попытка прочитать несуществующий файл

