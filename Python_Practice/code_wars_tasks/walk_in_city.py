# n - s - два направления север и юг ; w - e - запад восток

a = ['n','s','n','s','n','s','n','s','n','s']

def is_valid_walk(walk):
    if len(walk) != 10 :
        return False
    if (walk.count('n') == walk.count('s')) and (walk.count('w') == walk.count('e')):
        return True
    else:
        return False 

print(is_valid_walk(a))