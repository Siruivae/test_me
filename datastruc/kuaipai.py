def quick_sort(s, start, end):
    if start < end:
        i, j, pivot = start, end, L[start]
        while i<j:
            if s[j] < pivot:
                s[i] = s[j]
                i = i-1
            else:
                j = j-1
            if s[i] > pivot:
                s[j] = s[i]
                j = j - 1
            else:
                i = i + 1

        s[i] = pivot
        quick_sort(L, start, i-1)
        quick_sort(L, i+1, end)
