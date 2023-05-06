#Отрицательная степень через функцию 
def degree(a,n) :
    if n == 0 :
        return 1 
    elif n > 0 :
        a_sum = a
        for i in range(n-1) :
            a_sum *= a
        return a_sum
    else :
        a_sum = a
        for i in range(abs(n)-1) :
            a_sum *= a
        return 1/(a_sum)

a = float(input())
n = int(input())
print (degree(a,n))
