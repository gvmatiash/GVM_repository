n = input()

for i in range(n.find('h')) :
    print(n[i], sep='', end='')
for i in range(n.rfind('h') + 1, len(n)) :
    print(n[i], sep='', end='')