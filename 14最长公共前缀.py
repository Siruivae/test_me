class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]



'''class chao():
    def zu(self, strs):
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(len(strs)):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
                
    def lcp(self, str1, str2):
        count = min(len(str1), len(str2))
        i = 0
        for i in range(count):
            if str1(i) == str2(i):
                i +=1
            return str1[:i]'''
print("hello2")
