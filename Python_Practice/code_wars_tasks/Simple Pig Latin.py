import string

def pig_it(text):
    words = []
    for word in text.split():
        if word not in string.punctuation:
            words.append(word[1:] + word[0] + 'ay')
        else:
            words.append(word)
    return ' '.join(words)

print(pig_it('Hello world !')) 
