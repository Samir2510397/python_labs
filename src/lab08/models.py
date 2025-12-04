from dataclasses import dataclass
from datetime import datetime, date


@dataclass# Генрируем класс с аргументами
class Student:
    FullName: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):#Проверяем дату и балл на корректность
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {self.birthdate}, требуется: YYYY-MM-DD")

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть от 0 до 5. Вы ввели: {self.gpa}")

    def age(self) -> int:#Вычисляем возраст
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def to_dict(self) -> dict:#Сереализация
        return {
            "FullName": self.FullName,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):#Десереализация
        return cls(
            FullName=data["FullName"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )

    def __str__(self) -> str:#Переделываем все в строки
        return (
            f"{self.FullName}\n"
            f"Дата рождения: {self.birthdate}\n"
            f"Группа: {self.group}\n"
            f"Средний балл: {self.gpa}"
        )


if __name__ == "__main__":
    student = Student("Абдуллин Самир Ниязович", "2007-06-07", "БИВТ-25-3", 5.0)#Создаем с валидацией
    print(student)#Выводим черес строки
    print("=" * 140)#Разделяем

    print(f"Возраст: {student.age()}")

    student_dict = student.to_dict()#Сереализируем в словарь
    print(f"Сериализованный: {student_dict}")

    restored_student = Student.from_dict(student_dict)#Десереализируем в словарь с валидацией
    print(f"Десериализованный: {restored_student}")