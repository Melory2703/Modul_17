tickets = int(input("Введите количество билетов: "))
summ = 0
prise = " "
for i in range(1, tickets + 1):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        prise = 0
    elif 18 <= age < 25:
        prise = 990
    else:
        prise = 1390
    summ += prise
if tickets > 3:
    discount = summ / 10
    summ = summ - discount
    print("Сумма к оплате с учетом 10% скидки составляет: ", summ, "руб.")
else:
    print("Сумма к оплате составляет: ", summ, "руб.")