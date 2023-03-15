tickets = int(input("Введите количество билетов: "))
summ = 0
price = " "
for i in range(1, tickets + 1):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
    summ += price
if tickets > 3:
    discount = summ / 10
    summ = summ - discount
    print("Сумма к оплате с учетом 10% скидки составляет: ", summ, "руб.")
else:
    print("Сумма к оплате составляет: ", summ, "руб.")
