# Длина линии между двумя точками
from math import sqrt 

def line_length(array) :
    if len(array) == 4 :
        x1, y1, x2, y2 = array
        b = sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2)
        return b
    else : 
        print('Ошибка: неверно указано количество переменных')
a = []
for i in range(4) : 
    a.append(float(input()))

print(line_length(a))
 