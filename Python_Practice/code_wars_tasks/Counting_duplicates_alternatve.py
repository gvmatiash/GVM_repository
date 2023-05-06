
def duplicate_count(text):
    unique = set()
    [unique.add(elem) for elem in text.lower()]
    a = [text.count(letter.lower()) for letter in unique if text.count(letter.lower()) > 1]
    return len(a)

print(duplicate_count('Indivisibilities'))