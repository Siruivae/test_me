class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
           return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        count = min(len(str1), len(str2))
        i = 0
        while i < count and str1[i] == str2[i]:
                i += 1
        return str1[:i]
s = Solution2()
L1 = ["dog","racecar","car"]
L2 = ["flower","flow","flight"]
L3 = ["abc", "abc", "abc"]
a = s.longestCommonPrefix(L3)
print(a)