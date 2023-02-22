import random

target = ['X' for i in range(10)]
goal = random.randrange(1,10)

def draw_target(target):
    print(*target)
    
def try_shoot(target):
    while True:
        target_number = input('Введите порядковый номер мишени для выстрела\n')
        if target_number.isdigit() and (0 <= int(target_number) <= len(target)):
            if target[int(target_number)-1] != 'X':
                print('В эту область уже стреляли!')
            else:
                break
        else:
            print('Нужно указать число от 0 до 10')
    return target_number        
        

def main(goal):
    print('Попробуй как можно быстрее найти правильную мишень!')
    counter = 0
    while True:
        draw_target(target)
        hited_target = try_shoot(target)
        if int(hited_target) == goal:
            print('Вы угадали, с победой!')
            print(f'Число попыток = {counter}')
            break
        else:
            target[int(hited_target)-1] = 'O'
            print('Мимо!')
            counter += 1

        
main(goal)


