def is_leap_year(year):
	if year % 4 == 0:
		return True
	else:
		return False

year = int(input("Введите год: "))

if is_leap_year(year):
	print(True)
else:
	print(False)