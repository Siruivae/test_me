def zj(l):
    for i in range(1, len(l)):
        for j in range(i-1,-1, -1):
            if l[j] > l[i]:
                exchange

def xier(l):
    d =d//2
    while d>0:
        for i in range(d, len(l)):
            if l[i] < l[i-d]:
                tmp = l[i]
                j = i-d
                while j >0 and tmp < l[j]:
                    l[j] = l[j+d]
                    j = j-d
                l[j+d] = tmp
        d = d//2
def maopao(l):
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[i] > l[i+1]:
def kuai(l, s, e):
    if s < e:
        i, j, base=s, e, l[s]
        while i <j:
                while i<j and l[j] >= base:
                    j = j-1
                if i<j:
                    l[i] = l[j]
                    i = i+1
                while i<j and l[i] < base:
                    i = i+1
                if i<j:
                    l[j] = l[i]
                    j = j-1
        l[i] = base
        kuai(l, s, i-1)
        kuai(l, i+1, e)

def jiandan(l):
    for i in range(len(l)):
        min = l[i]
        for j in range(i+1, len(l)):
            if l[j] < min:
        l[i] = min