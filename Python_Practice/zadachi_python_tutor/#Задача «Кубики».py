#Задача «Кубики»
#N - число кубиков Ани, M - число кубиков Бори
#Найти 1) номера, которые есть в обоих множествах
# 2) номера, которые есть только у ани
# 3) номера - только у Бори.
# Вывод: сначала кол-во элементов, затем элементы по возрастанию
def print_set(any_set) :
    print(len(any_set))
    print(*sorted(any_set))

N, M = [int(num) for num in input().split()]
numbers_Ann = set()
numbers_Borya = set()

for i in range(N) :
    numbers_Ann.add(int(input()))
for i in range(M) :
    numbers_Borya.add(int(input()))

print_set(numbers_Ann & numbers_Borya)
print_set(numbers_Ann - numbers_Borya)
print_set(numbers_Borya - numbers_Ann)

