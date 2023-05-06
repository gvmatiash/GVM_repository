#Задача «Выборы в США»
votes = {}
for i in range(int(input())) :
    candidate , points = input().split()
    # if candidate in votes :
    #     votes[candidate] += int(points)
    # else: 
    #     votes[candidate] = int(points)
    votes[candidate] = votes.get(candidate, 0) + int(points)


for key, val in sorted(votes.items()) :
    print (key, val)
