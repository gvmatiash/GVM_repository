# Задача «Страны и города» (2 решение)
countries = {}

for i in range(int(input())) :
    capital , *cities = input().split()
    for city in cities :
        countries[city] = capital

for j in range(int(input())) :
    print(countries[input()])
