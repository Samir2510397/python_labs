import json
from src.lib import Student


def students_to_json(students: list[Student], path: str) -> None:#Преобразуем все в словарь и записываем в json файл
    students_data = [student.to_dict() for student in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[Student]:#Читаем файл и создаем объекты для каждого словаря, а также обрабатываем ошибки
    try:
        with open(path, 'r', encoding='utf-8') as f:
            students_data = json.load(f)

        students = [Student.from_dict(data) for data in students_data]
        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []


def test_serialization():#Тестируем и сохраняем в json файле
    students = students_from_json('data/lab08/lab08_input.json')
    print("\n Загруженные студенты:")
    for student in students:
        print(f"FullName: {student.FullName}, birthdate: {student.birthdate}, group: {student.group}, GPA: {student.gpa}")
    print("\n Сохранение в выходной файл")
    students_to_json(students, 'data/lab08/lab08_output.json')
    print("Файл сохранен: data/lab08/lab08_output.json")


if __name__ == "__main__":
    test_serialization()