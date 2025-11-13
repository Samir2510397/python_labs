import argparse
from pathlib import Path
from src.lib import tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")#Создаем парсер с описанием для справки
    subparsers = parser.add_subparsers(dest="command")#Создаем группу подпарсеров для разных команд и выбранная команда сохранится в args.command

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()#Парсим аргументы командной строки

    file = Path(args.input)#Создаем объект Path для работы с путём файла

    if not file.exists():#Проверяем существование файла, иначе выбрасывает исключение
        raise FileNotFoundError("Файл не найден")

    if args.command == "cat":
        # py -m src.lab06.cli_text cat --input data/samples/text.txt -n

        with open(file, "r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":
        # py -m src.lab06.cli_text stats --input data/samples/text.txt --top 3

        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]
        data = "".join(data)

        tokens = tokenize(data)
        freq = count_freq(tokens)
        top = top_n(freq, args.top)

        print(f"Топ-{args.top} слов в файле '{args.input}':")
        number = 1
        for word, count in top:
            print(f"{number}. '{word}' - {count} раз")
            number += 1


if __name__ == "__main__":
    main()