#Задача "Забастовки"
#Функция, которая будет добавлять во множество дополнительные дни
def extend_dict(day : int, step : int, all_days : set, year_length : int ) :
    while day <= year_length :
        all_days.add(day)
        day += step
    return all_days
     

N, K = [int(s) for s in input().split()]
all_days = set()

#Для каждой введенной забастовки с условием выполняем функцию, которая дополняет множество
for i in range(K) :
    day , step = [int(s) for s in input().split()]
    all_days = extend_dict(day, step, all_days, N)

# выкидываем из множества все числа, кратные 6 и 7 - то есть выходные дни
to_remove = set()
for elem in all_days :
    #ГЕНИАЛЬНО!!! Остаток от деления на семь равно 6 - даст субботу
    if (elem % 7 == 6) or (elem % 7 == 0) :
        to_remove.add(elem)
all_days.difference_update(to_remove) 

print(len(all_days))
