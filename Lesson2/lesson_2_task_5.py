def month_to_season(month):
    if month == 12 or 0 < month <= 2:
        print("Зима")
    elif 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <= 8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    else:
        print('Введенный номер месяца может быть только от 1 до 12 включительно.')
        return month

month = int(input("Введите номер месяца от 1 до 12: "))

month_to_season(month)