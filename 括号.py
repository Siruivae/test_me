#from inspect import stack

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                #如果不是相同的类型，或者栈中并没有左括号，
                #那么字符串无效，返回 False。
                stack.pop()  #出栈
            else:
                stack.append(ch)  #进栈

        return not stack


class Solution2:
    def kuohao(self, s):
        if len(s) % 2 == 1:
           return False
        paris = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in paris:
                if not stack or paris[ch] != stack[-1]
                    return False
            else:
               stack.append()
        return not stack


class shushang:
    def ismatch(self, str):
        st = stack()
        i = 0
        while i < len(str):
            e = str[i]
            if e =='(' or e =='[' or e == '{':
                st.push(e)
            else:
                if e ==')':
                    if st.empty() or st.gettop() != '(':
                        return False
                    st.pop()
                if e == ']':
                    if st.empty() or st.gettop() != '[':
                        return False
                    st.pop()
                if e == '}':
                    if st.empty() or st.gettop() != '{':
                        return False
                    st.pop()
            i +=1
        return st.empty()

class July():
    def kuohao(self, s):
        dict = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
