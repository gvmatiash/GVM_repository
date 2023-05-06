# Задача «Частотный анализ»

all_words = {}

#Считываем строки и записываем их в массив
for i in range(int(input())) :
    for word in input().split() :
        all_words[word] = all_words.get(word , 0) + 1

for key , val in all_words.items() :
    all_words[key] = (all_words.get(key), key)

sorted_words = sorted(all_words.values(), key=lambda x: (-x[0], x[1]) )


for number , key in sorted_words :
    print(key)    





