#Ферзи
column_array = []
line_array = []

# создадим два массива: первый - с номером колонки, второй - номер строки. 
for i in range(8) :
    column , line = [int(s) for s in input().split()]
    column_array.append(column)
    line_array.append(line)

# Правила, по которым понимаем, что ферзи бьют друг друга
# 1) цифры массива столбцов повторились (или сумма == 36)
# 2) цифры массива строк повторились (или сумма == 36)
# 3) разница двух элементов массивов с одинаковыми индексами
# 4) сумма двух элементов массивов с одинаковыми индексами

diff_array = [] # массив для подсчета "3)"
sum_array = [] # массив для подсчета "4)" - суммы элементов двух массивов
search = False

#1 - 2 условие проверяем
if (sum(column_array) != 36) or (sum(line_array) != 36) :
    search = True
else : # 3 и 4 условие проверяем
    for i in range(8) :
        diff_array.append(column_array[i] - line_array[i])
        sum_array.append(column_array[i] + line_array[i])
    for i in range(8) :
        for j in range(8) :
            if ((diff_array[i] == diff_array[j]) and (i != j)) :
                search = True 
                break
            if ((sum_array[i] == sum_array[j]) and (i != j)) :
                search = True
                break
if search == False :
    print('NO')
else: 
    print('YES')

    

            

