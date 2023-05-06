#Задача «Поменять столбцы»
#a - массив, i - столбец 1, j - столбец 2
def swap_columns(a, i, j) :
    for row in range(len(a)) :
        a[row][i], a[row][j] = a[row][j], a[row][i]
    return (a)

n , m = [int(s) for s in input().split()]

a = [[int(elem) for elem in input().split()] for i in range(n)]

i , j = [int(s) for s in input().split()]

ready = swap_columns(a,i,j)
for row in ready :
    print(' '.join([str(elem) for elem in row]))