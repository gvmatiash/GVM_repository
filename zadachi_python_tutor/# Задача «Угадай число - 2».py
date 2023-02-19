# Задача «Угадай число - 2»

n_max = int(input())
all_numbers = set(range(1 , n_max + 1))

guess = input()

while guess != 'HELP' :
    guess_dict = set([int(num) for num in guess.split()])
    
    if len(all_numbers & guess_dict) <= (len(all_numbers) // 2) :
        print('NO')
        all_numbers.difference_update(guess_dict)
    else :
        print('YES')
        all_numbers &= guess_dict
    guess = input()

print(*sorted(all_numbers))