# Функция преобразует строку-скрамбл в список элементов
def transform_scrumble(some_string : str):
    pass

# Словарь трансформации по X
x_converter = {
    'R' : 'R',
    'L' : 'L',
    'U' : 'B',
    'D' : 'F',
    'F' : 'U',
    'B' : 'D',
    'r' : 'r',
    'l' : 'l',
    'u' : 'b',
    'd' : 'f',
    'f' : 'u',
    'b' : 'd',
    'M' : 'M',
    'E' : 'S',
    'S' : 'E\'',
}


new_scrumble = []
#на вход берем строку из комбинаций и в цикл конвертируем через словарь: ключ-значение
for elem in input('Введите последовательность движений\n'):
    new_scrumble.append(x_converter.get(elem))
print(new_scrumble)
