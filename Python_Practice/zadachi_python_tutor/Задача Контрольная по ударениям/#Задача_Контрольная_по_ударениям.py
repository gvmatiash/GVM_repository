#Задача «Контрольная по ударениям»
def capitalized(word) :
    count_letters = 0
    for letter in word :
        if letter.islower() == False :
            count_letters += 1 
    return count_letters

N = int(input())

dictionary = {}
counter = 0

for i in range(N) :
    word = input()
    dictionary.setdefault(word.lower(), []).append(word)

for elem in input().split() :
    el_lo = elem.lower()
    if (elem not in (dictionary.get(el_lo, ''))) and (el_lo in dictionary.keys()):
        counter += 1
    elif (el_lo == elem) :
        counter += 1 
    elif capitalized(elem) > 1 :
        counter += 1
        
print(counter)