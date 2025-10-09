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