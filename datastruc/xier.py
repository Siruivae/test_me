def xier(L):
    x = len(L)
    g = (int)(x/2)   #整型
    while (g >= 1):
        for i in range(g):
            if L[1] >L[i+g]:
                tmp = L[i]
                L[1] = L[i + g]
                L[i + g] = tmp
        g /=2
    for j in range(1, x):
        for k in range(x-1, -1, -1):
            if L[k] >L[k+1]:
                tmp = L[k]
                L[k] = L[k+1]
                L[k+1] = tmp

def xier(l):
    d = len(l)//2
    while d>0:
        for i in range(d, len(l)):
            if l [i] < l[i-d]:
                tmp = l[i]
                j = i-d
                while j > 0 and tmp < l[j]:
                    l[j+d] = l[j]
                    j = j-d
                l[j+d] = tmp
        d = d//2
