#Задача «Номер появления слова»

all_words = dict()

for word in (input().split()) :
    if word in all_words :
        all_words[word] += 1
    else :
        all_words[word] = 0
    print(all_words.get(word), end=' ')

