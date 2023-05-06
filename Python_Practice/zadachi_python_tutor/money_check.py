print('Как вас зовут?')
thename = input()
print('Добрый день, ' + thename  + ', рад вас видеть! =)' )
print('Давайте считать сколько купюр в пачке денег')
print('Укажите общую сумму')
summa = int(input())
print('Укажите номинал купюры')
nominal = int(input())
rezult = summa // nominal
ostatok = summa - rezult * nominal
print('В общей сумме: ' + str(summa) + ', находится ' + str(rezult) + ' купюр, с номиналом ' +  str(nominal))
print('Остаток при этом составит: ' + str(ostatok))
