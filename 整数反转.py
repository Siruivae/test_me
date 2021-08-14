class solution:
    def fanzhuan1(self, x):
        if -10<x<10:
            return x
        x = str(x)
        if x[0]!='1':
            str_x = x[::-1]
            x = int(str_x)
        else:
            str_x = x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0

    def reverse_better(
                self,
                x: int) -> int:

            y, res = abs(x), 0
            # 则其数值范围为 [−2^31,  2^31 − 1]
            boundry = (1 << 31) - 1 if x > 0 else 1 << 31
            while y != 0:
                res = res * 10 + y % 10
                if res > boundry:
                    return 0
                y //= 10
            return res if x > 0 else -res

'''
def cuo(self, x):
    flag = 1
    i = 0
    if x< 0:
        x = -x
        flag = -1
    x = list(x)
    n = len(x)
    tmp = 0
    while i<n:
        tmp = x[i]
        x[n-i+1] = x[i]
        x[i] = tmp
        i +=1
    int(x)
    x = x*flag
    return x
print()'''

s = solution()
s.fanzhuan1(234)