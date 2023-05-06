def tree_check(first_name : str, second_name : str, some_tree : dict) :
    check_number = 0
    first_name_save = first_name
    while first_name in some_tree.keys() :
        if some_tree.get(first_name) == second_name :
            return 2
        first_name = some_tree.get(first_name)
    while second_name in some_tree.keys() :
        if some_tree.get(second_name) == first_name_save :
            return 1
        second_name = some_tree.get(second_name)    
    return check_number

family_tree = {}

for i in range(int(input()) - 1) :
    children_name , parent_name = input().split()
    family_tree[children_name] = parent_name

for k in range(int(input())) :
    left_name, right_name = input().split()
    print(tree_check(left_name,right_name,family_tree))



