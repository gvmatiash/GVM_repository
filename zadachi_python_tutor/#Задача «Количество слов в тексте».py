#Задача «Количество слов в тексте разделенных пробелом или переносом строки»
n = int(input())
words = set()

for i in range(n) :
    a = set(input().split())
    words |= a

print(len(words))