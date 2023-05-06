#Кегельбан
#N - кегли от 1 до N ; K - броски шаров ; l - r диапазон сбитых шаров
#обязательно 1<=l<=r<=N 
#вывести II....II..I - последовательность сбитых кеглей

#считываем первые данные - N и K
N, K = [int(s) for s in input().split()]


#получаем заполненный массив с кеглями
array_ful = ['I'] * N
print(''.join(array_ful))
#считываем броски 
for i in range(K) :
    l , r = [int(s) for s in input().split()]
  
    for j in range(l - 1, r) :
        array_ful[j] = '.'

print(''.join(array_ful))


