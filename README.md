# python_labs
# P-O-R-SH-E  9-1-1

## Лабораторная работа 1

### Задание 1
```python
name = input()
age = int(input())
print('Имя:' + name)
print('Возраст:' + str(age))
print("Привет," + name + "!", " Через год тебе будет " + str(age+1) + ".")
```
![Картинка 1](./images/lab01/011.png)

### Задание 2
```python
for i in range(10):
    print("hello world")
a = input()
b = float(input())
print("a: " + a.replace('.', ','))
print("b: " + str(b))
print("sum=" + str((float(a)+b)) + ";" + " avg=" + str((float(a)+b)/2))
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

print("База после скидки: " + str(base) + " ₽")
print("НДС: " + str(vat_amount) + " ₽")
print("Итого к оплате: " + str(total) + " ₽")
```
![Картинка 3](./images/lab01/03.png)

### Задание 4
```python
m = int(input())
print('Минуты:' + ' ' + str(m))
print(str((m//60)) + ":" + str(m%60))
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
    elif form[i][3] == 'False': fl += 1
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
