class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0
       # y = x
        if (x % 10 !=0):
            while(x > r):
                r = r*10 +x%10
                x = x//10
        return r == x or x == r//10

if __name__ =='__main__':

    i = 121
#创建一个类，调用

'''r = 0
        y = x
        while(x !=0):
            r = r*10 +x%10
            x = x//10
        if (r == y):
            return true
        else:
            return false
class Solution:
    def isPalindrome(self, x: int) -> bool:'''
