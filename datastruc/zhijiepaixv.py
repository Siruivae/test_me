def direct(s):
    for i in range(1, len[s]):
        for j in range(i-1, -1, -1):   #开始，结束（不包括结束），补偿，这是逆序的写法
            if s[j] >s[i]:
                tmp = s[i+1]
                s[i] = s[j]
                s[i+1] = s[i]

def zhijie(l):
    for i in range(1, len(l)):
        for j in range(i-1, -1, -1):
            if l[j] > l[i]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp