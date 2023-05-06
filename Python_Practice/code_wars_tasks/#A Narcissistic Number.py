# A Narcissistic Number
num = int(input())


def is_Narcissitic(value):
    summa_num = sum([int(number) ** (len(str(value)))
                    for number in str(value)])
    if summa_num == value:
        return True
    else:
        return False


print(is_Narcissitic(num))
