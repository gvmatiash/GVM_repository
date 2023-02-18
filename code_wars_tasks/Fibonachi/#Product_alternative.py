def productFib(prod: int):
    fib_1, fib_2 = 0, 1
    while (fib_1 * fib_2) < prod:
        fib_1, fib_2 = fib_2, (fib_1 + fib_2)
    return [fib_1, fib_2, fib_1 * fib_2 == prod]


print(productFib(4895))
