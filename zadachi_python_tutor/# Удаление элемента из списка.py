#Кегельбан
#N - кегли от 1 до N ; K - броски шаров ; l - r диапазон сбитых шаров
#обязательно 1<=l<=r<=N 
#вывести II....II..I - последовательность сбитых кеглей

#считываем первые данные - N и K
array_one = [int(s) for s in input().split()]
N = array_one[0]
K = array_one[1]

#получаем заполненный массив с кеглями
array_ful = []
for i in range(N) :
    array_ful.append('I')

#считываем броски 
for i in range(K) :
    a = [int(s) for s in input().split()]
    l = a[0]
    r = a[1]
    for j in range(l - 1, r) :
        array_ful[j] = '.'

print(''.join([str(s) for s in array_ful]))


