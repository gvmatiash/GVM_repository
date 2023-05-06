# UpPeR CaSe

def to_weird_case(words):
    splited_words = words.split()
    result = []
    for word in splited_words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        result.append(new_word)
    return ' '.join(result)


print(to_weird_case('String is Upperpe'))
