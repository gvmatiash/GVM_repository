# Задача «Права доступа»           
def string_to_storage(some_string : str, dictionary_name : dict) :
    splited_string = some_string.split()
    dictionary_name[splited_string[0]] = splited_string[1 : ]
    return (dictionary_name)

commands_array = {'read' : 'R', 'write' : 'W' , 'execute' : 'X'}

storage = {}
for i in range(int(input())) :
    storage = string_to_storage(input(),storage)


for j in range(int(input())) :
    command , key = input().split()
    check = False
    for value in storage[key] :
        if value == commands_array[command] :
            check = True
            break
    if check == True :
        print('OK')
    else :
        print('Access denied')  

