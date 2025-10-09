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
    finite = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                finite.append(j)
        else:
            return 'TypeError'
    return finite



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
