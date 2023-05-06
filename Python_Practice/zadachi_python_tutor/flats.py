import math

flats = int(input('Какое кол-во квартир на одном этаже? \n'))
flat_number = int(input('Введите номер квартиры \n'))
result = math.ceil(flat_number / (flats))  

print (f"Кваритра с номером {flat_number} находится на {result}-м этаже")


