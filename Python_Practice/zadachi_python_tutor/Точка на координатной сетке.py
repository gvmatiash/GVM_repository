# Определение точки на оси
#Выясняем, в какой из 4 четвертей на координатной плоскости лежит точка с координатами (x.y)
print('Введите X')
x = int(input())
print('Введите Y')
y = int(input())
if x > 0 : 
    if y > 0 :
        print('Первая четверть')
    else : 
        print('Четвертая четверть')
else : 
    if y > 0 :
        print('Вторая четверть')
    else : 
        print('Третья четверть')