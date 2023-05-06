n = input()

print(n[ : n.find('h') + 1] , sep='', end='')
print (n[(n.rfind('h') - 1) : n.find('h') : -1] , sep='', end='')
print(n[n.rfind('h') : ])