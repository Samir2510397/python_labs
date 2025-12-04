import csv
from pathlib import Path
from src.lib import Student, students_from_json
from typing import List

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)#преобразуем строку в path
        self.fieldnames = ['FullName', 'birthdate', 'group', 'gpa']# Наши заголовки
        self._ensure_file_exists()#Создаем файл с заголовком

    def _ensure_file_exists(self):
        if not self.path.exists():#Если нет файла
            self.path.parent.mkdir(parents=True, exist_ok=True)#Создаем папки
            with open(self.path, 'w', encoding='utf-8', newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()#записываем заголовок

    def read_all(self) -> List[Student]:
        self._ensure_file_exists()
        students = []
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)#Читаем как словарь
            for row in reader:#Для каждой строки
                students.append(Student.from_dict(row))#Создаем студента
        return students

    def list(self)->list[Student]:#Возвращаем всех студентов
        return self.read_all()

    def add(self, student: Student):#Добавляем нового студента
        self._ensure_file_exists()
        with open(self.path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(student.to_dict())#Добавляем в конец файла

    def find(self, substr:str) -> List[Student]:
        students = self.read_all()#Читаем всех студентов
        l = []#Для результатов
        for st in students:
            if substr.lower() in st.FullName.lower():#проверяем есть ли подстрока в фио
                l.append(st)#Добавляем результаты
        return l

    def remove(self, FullName: str):#Читаем всех
        students = self.read_all()
        new_students = [st for st in students if st.FullName != FullName]#Список без удаляемого студента
        if len(students) != len(new_students):
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()#Перезапись заголовка
                for st in new_students:#Записываем всех кроме удаленного
                    writer.writerow(st.to_dict())

    def remove_all(self):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()

    def update(self, FullName: str, **ost):
        students = self.read_all()#читаем все
        flag = False#флаг нахождения студента
        for st in students:
            if st.FullName == FullName:#Если нашли то обновляем
                for key, value in ost.items():
                    if hasattr(st, key):#проверяем есть ли у студента поле
                        setattr(st, key, value)#устанавливаем новое значение
                flag = True
                break
        if flag:#если нашли и обновили
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for st in students:#перезаписываем всех студентов
                    writer.writerow(st.to_dict())



students = students_from_json('C:/Users/Samir/OneDrive/Документы/GitHub/python_labs/data/lab08/lab08_input.json')#Читаем файл и создаем объект студент и превращаем его в список
l = Group("test.csv")#создаем файл
l.remove_all()#чистим его
for i in students:#каждого студента добавляем в csv
    l.add(i)
print(*l.list(),sep='\n')#читаем и распаковываем всех
print('='*140)
print(*l.find("ин"),sep='\n')#ищем меня
print('='*140)
l.remove("Киселев Александр Игоревич")#кикаем саню
l.update("Абдуллин Самир Ниязович",birthdate = '2002-03-25',group='tsp-21-1',gpa=3.0)#превращаем меняя в старшекурсника-раздолбая











