import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold() #Весь текст в нижний регистр
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    while '   ' in text:
        text = text.replace('   ', ' ')#Тройные пробелы на одинарные и потом удаление
    return text.strip()


def tokenize(text: str) -> list[str]:
    text = text.replace('!', '')
    text = re.split(r'[^\w-]+', text)#Разбиение слов не по буквам и дефисам
    return text


def count_freq(tokens: list[str]) -> dict[str, int]:
    dic = {}# Делаем словарь
    unique = set(tokens) # Делаем множество
    for _ in unique:
        dic[_] = tokens.count(_)# Кол-во в слов в списке
    return dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))# сортируем элементы словаря по убыванию частоты и по алфавиту и преобразуем обратно в словарь


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]#сортируем пары из словаря по частоте в порядке убывания и берем первые n штук


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






