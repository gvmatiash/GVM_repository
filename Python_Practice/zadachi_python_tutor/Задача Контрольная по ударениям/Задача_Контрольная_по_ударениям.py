#Задача «Контрольная по ударениям»
N = int(input())

dictionary = {'cannot', 'cannOt'}
counter = 0
for i in range(N) :
#     dictionary.add(input())
    if input() in dictionary:
        counter += 1
print(counter)