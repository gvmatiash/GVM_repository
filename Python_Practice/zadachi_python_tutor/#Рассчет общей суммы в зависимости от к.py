# Рассчет общей суммы в зависимости от купюр
identificator = int(input('Выберите валюту: "1" - рубли, "2" - тенге\n'))

if identificator == 1 :
    currency = 'руб.'
elif identificator == 2 :
    currency = 'тенге'
else :
    print('Неверно указана валюта')
    StopIteration

denominations_tenge = (20000, 10000, 5000, 2000, 1000, 500, 100)
denominations_rub = (5000, 1000, 500)
summa = 0
if currency == 'руб.' :
    for elem in denominations_rub :
        summa += elem * int(input(f'Сколько есть купюр номиналом = "{elem}"?\n'))
elif currency == 'тенге' :
    for elem in denominations_tenge :
        summa += elem * int(input(f'Сколько есть купюр номиналом = "{elem}"?\n'))

print(f'Итого сумма = {summa} {currency}')


    