def move_zeros(lst):
    array = [e for e in lst if e != 0]
    for elem in lst:

        if elem == 0:

            array.append(elem)
    return array


test_array = [1, 0, 1,
              2, 0, 1, 3]
print(move_zeros(test_array))

print('move')
