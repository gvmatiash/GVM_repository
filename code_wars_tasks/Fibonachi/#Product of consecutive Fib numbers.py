# Функция возвращает число фибоначи, принимая его индекс
def fib_num(num: int):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib_num(num-1) + fib_num(num-2)

# Функция возвращает два соседних числа фибоначи,
# и проверку: равно ли их произведение числу на входе
def productFib(prod):
    fib_1_ind, fib_1 = 0, 0
    fib_2_ind, fib_2 = 1, 1
# пока их произведение меньше заданного числа
    while (fib_1 * fib_2) < prod:
        fib_1_ind += 1
        fib_2_ind += 1
        fib_1 = fib_num(fib_1_ind)
        fib_2 = fib_num(fib_2_ind)
        check = [fib_1*fib_2 == prod]
    return [fib_1, fib_2, *check]


print(productFib(5895))
