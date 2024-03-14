def bank(x, y):
    for each_year in range(y):
        x = (x * 1.1)
    return x
x = int(input('Введите сумму вклада: '))
y = int(input('Введите срок вклада: '))

print("Сумма за указанный период составляет: ", bank(x, y))