def bank(contribution, time):
    for each_year in range(time):
        contribution = (contribution * 1.1)
    return contribution
contribution = int(input('Введите сумму вклада: '))
time = int(input('Введите срок вклада: '))

print("Сумма за указанный период составляет: ", bank(contribution, time))