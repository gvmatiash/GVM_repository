flats = int(input('Какое кол-во квартир на одном этаже?'))
flat_number = int(input('Введите номер квартиры'))
result = (flat_number // (flats + 1))  

print (f"Кваритра с номером {flat_number} находится на {result}-м этаже")


