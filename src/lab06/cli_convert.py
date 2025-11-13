import argparse
from src.lib import json_to_csv, csv_to_json, csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")#Создаем основной парсер с описанием "Конвертеры данных"
    sub = parser.add_subparsers(dest="cmd")#Создаем группу подпарсеров для разных команд ,а выбор команды будет сохранен в атрибут cmd


    json_to_csv_p = sub.add_parser("json2csv")#Создаем подпарсер для команды json2csv
    json_to_csv_p.add_argument("--input", dest="input", required=True, help="Входной JSON файл")
    json_to_csv_p.add_argument("--output", dest="output", required=True, help="Выходной CSV файл")

    csv_to_json_p = sub.add_parser("csv2json")#Создаем подпарсер для команды csv2json
    csv_to_json_p.add_argument("--input", dest="input", required=True, help="Входной CSV файл")
    csv_to_json_p.add_argument("--output", dest="output", required=True, help="Выходной JSON файл")

    csv_to_xlsx_p = sub.add_parser("csv2xlsx")#Создаем подпарсер для команды csv2xlsx
    csv_to_xlsx_p.add_argument("--input", dest="input", required=True, help="Входной CSV файл")
    csv_to_xlsx_p.add_argument("--output", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()#Парсим аргументы командной строки и сохраняем в объект args

    if args.cmd == "json2csv":
        # py -m src.lab06.cli_convert json2csv --input  data/samples/ex1.json  --output data/out/ex1_from_json.csv
        json_to_csv(json_path=args.input, csv_path=args.output)
    elif  args.cmd == "csv2json":
        #py -m src.lab06.cli_convert csv2json --input data/samples/ex2.csv --output data/out/ex2_from_csv.json
        csv_to_json(csv_path=args.input, json_path=args.output)
    elif args.cmd == "csv2xlsx":
        #py -m src.lab06.cli_convert csv2xlsx --input data/samples/ex2.csv --output data/out/ex2_from_csv.xlsx
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)

if __name__ == "__main__":
    main()