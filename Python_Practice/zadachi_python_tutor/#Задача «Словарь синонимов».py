#Задача «Словарь синонимов»
synonyms = dict()

for i in range(int(input())) :
    key , val = input().split()
    synonyms[key] = val


guess = input()

if guess in synonyms :
    print(synonyms[guess])
else:
    for val in synonyms:
        if synonyms[val] == guess : 
            print(val)

