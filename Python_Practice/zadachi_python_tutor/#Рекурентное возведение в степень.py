#Рекурентное возведение в степень
#a = a * a**(n-1)
def power(a, n) :
    if n == 0 :
        return 1 
    else: 
        return a * power(a, n - 1)

a = 3
n = 4

print (power(a,n))

 