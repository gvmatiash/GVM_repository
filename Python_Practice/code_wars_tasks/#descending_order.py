#descending_order
x = '684184'

def descending_order(num) :
    return ''.join(sorted(num,reverse=True))
 
print(descending_order(x))