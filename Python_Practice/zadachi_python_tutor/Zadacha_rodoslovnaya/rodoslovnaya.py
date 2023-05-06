from collections import defaultdict

family_tree = defaultdict(lambda : [])
people = set()

def order(some_name : str, some_tree : dict) :
    order_num = 1
    if some_name not in some_tree.keys():
        order_num = 0
    while some_tree.get(some_name) in some_tree.keys() :
        order_num += 1
        some_name = some_tree.get(some_name) 
    return order_num


for i in range(int(input()) - 1) :
    children_name , parent_name = input().split()
    family_tree[children_name] = parent_name
    people.add(children_name)
    people.add(parent_name)


for elem in sorted(people) :
    print(elem, order(elem, family_tree))

