#capitalize = заглавная буква для строк

def capitalize(word) :
    return (chr(ord(word[0]) - 32) + word[1:])


sentense = [str(s) for s in input().split()]

for i in range(len(sentense)) : 
    print (capitalize(sentense[i]), end=' ')
