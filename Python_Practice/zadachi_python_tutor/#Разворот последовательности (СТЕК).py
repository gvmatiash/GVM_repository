#Разворот последовательности (СТЕК)
# Функция стека работает так, что когда мы обращаемся к функции внутри себя (рекурсия) программа запоминает эту переменную, а потом пойдет в обратном порядке
# выше - мое объяснение (тупое, но как я понял с первого раза)

def reverse() :
    n = int(input())
    if n != 0 :
        reverse()
    print(n)

reverse()




