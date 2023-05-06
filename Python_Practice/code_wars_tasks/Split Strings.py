def solution(s:str):
    splited_s = []
    if len(s) % 2 == 0:
        for i in range(0,len(s),2):
            splited_s.append(s[i:i+2]) 
    else:
        for i in range(0,len(s),2):
            if i == len(s)-1:
                splited_s.append(s[i]+'_')
            else:
                splited_s.append(s[i:i+2])
    return splited_s

print(solution('abc'))
print(solution('abcdef'))
