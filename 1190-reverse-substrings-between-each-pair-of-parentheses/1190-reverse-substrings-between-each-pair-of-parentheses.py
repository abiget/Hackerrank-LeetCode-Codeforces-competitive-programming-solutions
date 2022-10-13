class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        i,j = 0, len(s)
        stack = []
        while i < j:
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                index = stack.pop()
                s = s[:index+1] + s[i-1:index:-1] + s[i:]
            i += 1
        return "".join([i for i in s if i not in ['(', ')']])