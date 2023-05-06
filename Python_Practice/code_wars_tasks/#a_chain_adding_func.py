#a_chain_adding_func

 
s = 0

def add(number):
    def add_number(num):
        return num + number
    return add_number

print(add(1)(2))


