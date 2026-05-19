from datetime import date

MONTHS = {
    1: "ene",
    2: "feb",
    3: "mar",
    4: "abr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "ago",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dic",
}


def change_str_date(date_obj: date):
    day = date_obj.day
    month = MONTHS.get(date_obj.month, "")
    year = date_obj.year
    return f"{day:02d}-{month}.-{year}"
