n = input()
amount = n.count('f')

if amount > 1 :
    print ( n.find('f', n.find('f') + 1) )
elif amount == 1 :
    print('-1')
else : 
    print('-2')
