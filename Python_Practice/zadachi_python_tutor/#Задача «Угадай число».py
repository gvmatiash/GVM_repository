#Задача «Угадай число»

n_max = int(input())
number_true = set()

for i in range(1, n_max + 1) :
    number_true.add(str(i))


n = set(input().split())
stop = {'HELP'}

while (n.issuperset(stop)) == False:
    validator = input()
    if validator == 'YES' :
        number_true.intersection_update(n)
    else :
        number_true -= n
    n = set(input().split())

print(*sorted(number_true))