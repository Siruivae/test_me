def del(L, i, k):
    #直接把后面的元素前移
    for j in range(i + k, len(L)):
        L[j-k] = L[j]
    L.size-=k

#删除元素=x的数
#用新建列表的方法
def del_same(L, x):
    k = 0
    for i in range(len(L)):
        if L [i]!=x:
            L[k] = L[i]
            k = k+1
    L.size = k
#删除的把办法
def del2(L, x):
    k= 0
    for i in range(len(L)):
        if L[i]!=x:
            L[i-k]=L[i]
        else:
            k+=1
    L.size-=k

#有序表归并
def merge(A, B):
    a = len(A)
    b = len(B)
    for i in range(a):
        for j in range(b):
            if A[i] < b[j]:

