#Задача «Пересечение множеств»
AB = (list((set(list(input().split())) & set(list(input().split())))))

a = [int(s) for s in AB]
for i in range(len(a)) :
    print(min(a), end=' ')
    a.remove(min(a))
#for i in range(len(a)) :
#    print(a.pop(min(a)))
