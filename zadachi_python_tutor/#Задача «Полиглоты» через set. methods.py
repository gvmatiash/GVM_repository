#Задача «Полиглоты» через set. methods 

students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone = set.intersection(*students)
known_by_someone = set.union(*students)

print (len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print (len(known_by_someone), *sorted(known_by_someone), sep='\n')