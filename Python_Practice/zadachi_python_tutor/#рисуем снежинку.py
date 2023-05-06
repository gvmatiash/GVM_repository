#рисуем снежинку
n = int(input('Введите нечетное число'))
a = [['.']*n for i in range(n)]

for i in range(n) :
    for j in range(n):
        if i == j or (i == (n // 2)) or (j == (n // 2)) or (i + j == n - 1) :
            a[i][j] = '*'
        print(a[i][j], end=' ')
    print('')
