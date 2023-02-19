#Задача «Полиглоты»
def print_len_and_array(some_language) :
    print(len(some_language), *sorted(some_language), sep='\n')


sum_schoolers = int(input())
all_languages = set()
united_language = set()
schooler_languages = set()

for schooler in range(sum_schoolers) :
    for language_number in range(int(input())) :
        language = set(input().split())
        all_languages.update(language)
        schooler_languages.update(language)
    united_language = all_languages & schooler_languages
    set.clear(schooler_languages)

print_len_and_array(united_language)
print_len_and_array(all_languages)

