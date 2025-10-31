import sys
from src.lib import normalize, count_freq, top_n
text = input() # "Привет, мир! Привет!!!"
tokens = []
for word in normalize(text).split():# нормализуем и разбиваем слова
    clean_word = word.strip('.,!!!!?;:"()[]{}')# убираем лишние символы
    if clean_word:
        tokens.append(clean_word)# чистые слова добавляем в список

total_words = len(tokens)# кол-во слов
unique_words = len(count_freq(tokens))# уникальные слова
top_words = top_n(count_freq(tokens), 5)# 5 самых испульзуемых слов
print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")
for word, count in top_words:
        print(f"{word}:{count}")# пишем самые популярные слова и их количество
# "Привет, мир! Привет!!!"









