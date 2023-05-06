#Функция, возвращающая сумму чисел
import time

def funtion_time(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        start = func()
        end_time = time.time()
        result_time = end_time - start_time
        print(result_time)
        return start
    return inner_func

@funtion_time
def sum_numbers(num_1 : int, num_2  : int):
    return (num_1) + (num_2)



sum_numbers(4,6)


