#максимальный элемент в массиве (индексы этого элемента)
n, m = [int(s) for s in input('Введите число строк и столбцов через пробел').split()]
print('Введите массив данных')
a = [[int(s) for s in input().split()] for i in range(int(n))]

max_index_row = 0
max_index_column = 0
max_number = a[0][0]

for i in range(n) :
    for j in range(m) :
        if a[i][j] > max_number :
            max_index_row = i
            max_index_column = j
            max_number = a[i][j]

print('Максимальное число = ' + str(a[max_index_row][max_index_column]))
print('Оно находится в ' + str(max_index_row + 1) +'-й строке, '+ str(max_index_column + 1)+'-м столбце')
