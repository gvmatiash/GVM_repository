#RGB To Hex Conversion
def rgb(r,g,b):
    number = [r, g, b]
    a = ['{:02}'.format(hex(int(x))[2:].upper()) for x in number]
    return ''.join(a)



print(rgb(1, 2, 3))
print(rgb(-20, 275, 125))
print(rgb(255, 0, 255))

