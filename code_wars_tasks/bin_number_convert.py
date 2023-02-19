a = '1234'
# возвращаем количество 1 в бинарном исчислении числа
def bin_calc(num):
    return str(bin(int(num))).count('1')

print(bin_calc(a))
