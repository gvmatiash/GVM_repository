#Задача «Побочная диагональ»
n = int(input())
a = [[0]*n for row in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1 :
            a[i][j] = 1
        elif i + j > n - 1:
            a[i][j] = 2
        else :
            a[i][j] = 0
for row in a : 
    print(' '.join([str(elem) for elem in row]))