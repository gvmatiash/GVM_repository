
def duplicate_count(text):
    #добавим счетчик и словарь
    counter = 0
    repeated_letters = {}
    #буква из заданной строки станет ключем словаря, 
    # а количество вхождений = значению
    for letter in text.lower():
        repeated_letters[letter] = repeated_letters.setdefault(letter, 0) + 1 
    for key in repeated_letters:
        if repeated_letters.get(key) > 1:
            counter += 1
    return counter


    

print(duplicate_count('abcde'))
print(duplicate_count('aabbcde'))
print(duplicate_count('aabBcde'))
print(duplicate_count('Indivisibilities'))
