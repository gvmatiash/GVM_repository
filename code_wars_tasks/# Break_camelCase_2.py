# Break_camelCase_2
s = 'soooFoooCuuuCoo'
def break_camel(some_string):
    return ''.join(' '+letter if letter.isupper() else letter for letter in some_string )

print(break_camel(s))
