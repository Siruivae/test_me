def maopao(s):
    l = len(s)
    for x in range(1, l):
        for i in range(l-x):
            if s[i] > s[i+1]:
                tmp = s[i+1]
                s[i+1] = s[i]
                s[i] = tmp

'''#冒泡排序
def bubble_sort(L):
    length = len(L)
#序列长度为length，需要执行length-1轮交换
    for x in range(1,length):
#对于每一轮交换，都将序列当中的左右元素进行比较
#每轮交换当中，由于序列最后的元素一定是最大的，因此每轮循环到序列未排序的位置即可
        for i in range(0,length-x):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp'''
def maopao(l):
    for i in range(1, len(l)):
        for j in range(len(l) - i):
            if l[i] > l[i+1]:
                tmp = l[i+1]
                l[i+1] = l[i]