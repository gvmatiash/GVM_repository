N = input()

print('Длина строки - ' + str(len(N)) + ' символов.')
for i in range(len(N)+1) :
     print (str(1+i) + '-й символ - ' + str(N[i]))
