def solution(dic):
    l = dic.keys()
    l.sort()
    return l
dic = {2: 10, 4: 40, 1: 20, 3: 30}
print solution(dic)
