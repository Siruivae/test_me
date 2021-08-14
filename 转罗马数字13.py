'''class Solution:
    def romanToInt(self, s):
        d = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}   #要用大括号
        ret = 0
        ln = len(s)
        for i in range(ln):
            if i < ln - 1 and d[s[i]] < d[s[i + 1]]:
                ret -= d[s[i]]
            else:
                ret += d[s[i]]
        return ret'''
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000}
        n = len(s)
        i = 0
        j = 0
        s = 0
        for i in range(n):
            if dict[s[i]] < dict[s[i+1]]:

        while (i<n):
            for j in range(6):
                if str[i] == dict.item[j]:
                    s +=dict[j]
        return s
