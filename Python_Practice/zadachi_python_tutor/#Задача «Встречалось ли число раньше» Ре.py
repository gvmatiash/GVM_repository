#Задача «Встречалось ли число раньше» Решение 2 от авторов
numbers = [int(num) for num in input().split()]
numbers_save = set()

for num in numbers :
    if num in numbers_save :
        print('YES')
    else : 
        print('NO')
        numbers_save.add(num)

