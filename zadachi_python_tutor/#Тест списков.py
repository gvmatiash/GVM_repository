#Переставить min и max
a = [int(a) for a in input("Введите числа через пробел. Поменяем местами min и max").split()]

#находим максимальный элемент и запоминаем его индекс, аналогично с минимальным
index_max = 0
index_min = 0

for i in range(len(a)) :
    if a[i] > a[index_max] :
        index_max = i
    if a[i] < a[index_min] :
        index_min = i

a[index_max] , a[index_min] = a[index_min] , a[index_max]

print(' '.join([str(s) for s in a]))

