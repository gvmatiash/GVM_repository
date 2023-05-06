def zeros(n):
    summa = 0
    i = 5
    while i < n:
        summa += n // i    
        i *= 5
    # n // 5 + n // 25
    return summa
print(zeros(1000)) 

# def factorial(n):
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
#     return factorial(n-1) * (n)

# for i in range(126):
#     counter = 0
#     fac_i = factorial(i)
#     for c in str(fac_i)[::-1]:
#         if c == '0':
#             counter += 1
#         else:
#             break
#     print(f'n = {i}, 0 = {counter}')
        

            


    