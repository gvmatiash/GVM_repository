import string

def pig_it(text):
    return ' '.join([word[1:] + word[0] + 'ay' if word not in string.punctuation else word for word in text.split()])

print(pig_it('Hello world !')) 
