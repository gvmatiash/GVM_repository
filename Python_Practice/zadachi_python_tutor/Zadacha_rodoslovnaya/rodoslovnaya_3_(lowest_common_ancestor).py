
def Lowest_Common_Ancestor(first_name : str, second_name : str, some_tree : dict) :
    parents_list = {}
    first_name_save = first_name
    second_name_save = second_name
    parents_list[first_name_save] = [first_name_save]
    parents_list[second_name_save] = [second_name_save]
    # заносим для 1_имени всех его предков, причем 1-й предок - он сам (условие задачи)
    while first_name in some_tree.keys() : 
        parents_list.setdefault(first_name_save, []).append(some_tree.get(first_name))
        first_name = some_tree.get(first_name)
    # заносим для 2_имени всех его предков, причем 1-й предок - он сам (условие задачи)
    while second_name in some_tree.keys() :
        parents_list.setdefault(second_name_save, []).append(some_tree.get(second_name))
        second_name = some_tree.get(second_name)
    # выясняем кол-во предков и определяем максимальный
    max_number = max(len(parents_list.get(first_name_save)),(len(parents_list.get(second_name_save))))
    # берем предков с начала(такой сложный процесс из-за того,
    # что изначально решал задачу для проверки с конца)
    # и ищем, кто из них будет первым общим для двух первоначальных имен
    for number in range(int(max_number)) : 
        try :
            name_to_check = parents_list.get(first_name_save)[number]
        except IndexError :
            name_to_check = ''
        if name_to_check in parents_list.get(second_name_save) :
            return name_to_check 
        else :
            try :
                name_to_check = parents_list.get(second_name_save)[number]
            except IndexError :
                name_to_check = ''
            if name_to_check in parents_list.get(first_name_save) :
                return name_to_check


family_tree = {}

for i in range(int(input()) - 1) :
    children_name , parent_name = input().split()
    family_tree[children_name] = parent_name


for k in range(int(input())) :
    left_name, right_name = input().split()
    print(Lowest_Common_Ancestor(left_name, right_name, family_tree))



