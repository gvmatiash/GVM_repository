a = '1234'

def bin_calc(num):
    return str(bin(int(num))).count('1')

print(bin_calc(a))
