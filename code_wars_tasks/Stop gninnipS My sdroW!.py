#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 

def spin_words(sentence):
    words = [x for x in sentence.split()]
    spinned_sentence = []

    for word in words :
        if len(word) > 4 :
            spinned_sentence.append(word[::-1])
        else:
            spinned_sentence.append(word)
          
    return ' '.join(spinned_sentence)


sent = input()
print(spin_words(sent)) 