tree = {'Alex' : ['Dsd'], 'Andrew' : ['Alex_1']}

first, second = input().split() 
for key in tree.keys() :
    if first in tree.get(key) :
        tree[key].append(second)      

if second not in tree.keys() :
    tree[second] = []

for elem in sorted(tree) :
    print(elem, len(tree.get(elem)))