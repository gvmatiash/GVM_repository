#Задача «Диагонали, параллельные главной»
n = int(input())
a = [[0]*n for row in range(n)]
# при помощи генераторов даный код можно упростить:
#a = [[abs(i-j) for j in range(n)] for i in range(n)] 

for i in range(n) :
    for j in range(n) :
            a[i][j] = abs(i - j)

for row in a :
    print(' '.join([str(elem) for elem in row]))