# Покупатель \ товар \ кол-во 
# Ivanov paper 10
from collections import defaultdict 
from sys import stdin

market = defaultdict(lambda : defaultdict(int))

for line in stdin.readlines() :
    client , item , amount = line.split()
    market[client][item] += int(amount)

for client in sorted(market) :
    print(client, ':')
    for item in sorted(market[client]) :
        print(item, market[client][item])