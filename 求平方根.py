class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = 1
        while left <= right:
            mid = left + (right-left)//2
            if mid**2 > x:
                right = right//2
        return mid

t=Solution()
t.mySqrt(6)