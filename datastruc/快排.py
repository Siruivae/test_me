#快速排序
#L：待排序的序列；start排序的开始index,end序列末尾的index
#对于长度为length的序列：start = 0;end = length-1
def quick_sort(L,start,end):
    if start < end:
        i , j , pivot = start , end , L[start]
        while i < j:
#从右开始向左寻找第一个小于pivot的值
            while (i < j) and (L[j] >= pivot):
                j = j-1
#将小于pivot的值移到左边
            if (i < j):
                L[i] = L[j]
                i = i+1
#从左开始向右寻找第一个大于pivot的值
            while (i < j) and (L[i] < pivot):
                i = i+1
#将大于pivot的值移到右边
            if (i < j):
                L[j] = L[i]
                j = j-1
#循环结束后，说明 i=j，此时左边的值全都小于pivot,右边的值全都大于pivot
#pivot的位置移动正确，那么此时只需对左右两侧的序列调用此函数进一步排序即可
#递归调用函数：依次对左侧序列：从0 ~ i-1//右侧序列：从i+1 ~ end
        L[i] = pivot
#左侧序列继续排序
        quick_sort(L,start,i-1)
#右侧序列继续排序
        quick_sort(L,i+1,end)
def q(l , s, e):
    if s<e:
        i,j,base=s, e, l[s]
        while i < j:
            while i<j and l[j] > base:
                j = j-1
            if i < j:
                l[i] = l[j]
                i = i + 1
            while i<j and l[i] <base:
                i = i+1
            if i<j:
                l[j] = l[i]
                j = j-1
        l[i] = base
        q(l, s, i-1)
        q(l, i+1, e)
