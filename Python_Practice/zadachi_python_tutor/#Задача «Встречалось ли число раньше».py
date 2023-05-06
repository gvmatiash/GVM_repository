#Задача «Встречалось ли число раньше»
a = input().split()
b = {'',}

for i in range(len(a)) :
    a_dict = {a[i]}
    if (a_dict <= b) == True :
        print('YES')
    else : 
        print('NO')
        b.update(a_dict)
