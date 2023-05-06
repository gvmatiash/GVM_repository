#Задача «Англо-латинский словарь» 
N = int(input())

l_e_dictionary = {}


for i in range(N) :
    definition, words = input().split(' - ')
    words = words.split(', ')
    for elem in words :
        l_e_dictionary.setdefault(elem , []).append(definition)

print(len(l_e_dictionary.keys()))

for key in sorted(l_e_dictionary.keys()) :
    print(key, '-', (', '.join(l_e_dictionary[key])))

