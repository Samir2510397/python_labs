import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        wb = Workbook()# создаем новую Excel кнгу
        ws = wb.active# получаем активный лист
        ws.title = "Sheet1"# переименовываем лист

        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)# создаем CSV reader
            for row in reader:# читаем острочно
                ws.append(row)# добавляем строку в Excel

        for column_cells in ws.columns:# проходим по каждому столбцу
            length = max(len(str(cell.value or "")) for cell in column_cells)#  находим макс длину текста в столбце
            ws.column_dimensions[column_cells[0].column_letter].width = max(length + 2, 8)# устанавливаем ширину минимум в 8 символов

        wb.save(xlsx_path)# сохраняем Excel файл

    except FileNotFoundError:
        raise FileNotFoundError