#Задача «Самое частое слово»
count_words = {}

for i in range(int(input())) :
    for word in input().split() :
        count_words[word] = count_words.get(word , 0) + 1

max_word_number = 0 


for key , val in sorted(count_words.items()) :
    if val > max_word_number :
        max_word_number = val
        count_words[val] = key

print(count_words.get(val))