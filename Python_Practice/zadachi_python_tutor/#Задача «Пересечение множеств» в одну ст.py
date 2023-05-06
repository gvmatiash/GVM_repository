#Задача «Пересечение множеств» в одну строку

print(*sorted(set(input().split()) & set(input().split()), key=int), end=' ')
