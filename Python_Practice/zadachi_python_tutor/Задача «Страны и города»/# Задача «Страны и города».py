# Задача «Страны и города»
countries = {}

for i in range(int(input())) :
    splited_string = input().split()
    capital = splited_string[0]
    for sity in splited_string[1:] :
        countries[sity] = capital
    

for j in range(int(input())) :
    print(countries[input()])
    