#Функции введение в тему
def maxi(*array) :
    maximum = array[0]
    for i in range(1, len(array)) :
        if array[i] > maximum :
            maximum = array[i]
    return maximum

array_B = [1,4,2,1,246,61,4,611,655,0,-2]

print(maxi(-3,2,33,24,0))
