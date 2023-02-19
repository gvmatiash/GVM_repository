# работа с массивом

a = input().split('.')

for i in range(len(a)) :
    if i == 2 : 
        print(int(a[2]) + 1, end='.')
    else :    
        print(a[i], end='.')
