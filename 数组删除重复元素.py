class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


class solution:
    def delete(self, nums):
        if not nums:
            return 0

        n = len(num)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        for i in range(n):
            for j in range(i+1, n):
                if num[i] != num[j]:
                    j += 1
                else:
                    num[j] = num[j+1]
                    k += 1
        return n-k+1

        n = len(nums)
        i = j = 1
        while i < n:
            if nums[i] != nums[i-1]:
                nums[k] = nums[j]
                j +=1
            i+=1
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] != nums[j]:
                    nums[k] = nums[j]
                    k+=1
        return l-k+1