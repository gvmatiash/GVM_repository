# Break camelCase
import re
s = 'SrseakSamelCase'
for letter in s:
    if letter.isupper():
        s = [s[0:s.find(letter)], s[s.find(letter):]]
        s[1] = re.findall('[A-Z][^A-Z]*', s[1])
        break
u = [s[0]]
for elem in s[1] :
    u.append(elem)
print((' '.join(u)).strip())




