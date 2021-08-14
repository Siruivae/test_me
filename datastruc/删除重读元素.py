class Solution:
    def removeDuplicates(self, nums):
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

a = [1, 2, 3, 4]
s = Solution()
s.removeDuplicates(a)