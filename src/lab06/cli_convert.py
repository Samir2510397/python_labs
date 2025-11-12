import argparse
from src.lib import json_to_csv, csv_to_json, csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    json_to_csv_p = sub.add_parser("json2csv")
    json_to_csv_p.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json_to_csv_p.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    csv_to_json_p = sub.add_parser("csv2json")
    csv_to_json_p.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv_to_json_p.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    csv_to_xlsx_p = sub.add_parser("csv2xlsx")
    csv_to_xlsx_p.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv_to_xlsx_p.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        #python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
        json_to_csv(json_path=args.input, csv_path=args.output)

    elif  args.cmd == "csv2json":
        #python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.cmd == "csv2xlsx":
        #python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)

if __name__ == "__main__":
    main()