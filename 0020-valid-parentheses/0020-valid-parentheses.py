class Solution:
    def isValid(self, s: str) -> bool:
        i,s = 0, list(s)
        open_char = ['(', '{', '[']
        match = ['()', '{}', '[]']
        stack = []
        while i<len(s):
            if s[i] in open_char:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    stack_smb = stack.pop()
                else:
                    stack_smb = 'dumy'
                if stack_smb+s[i] not in match:
                    return False
            i += 1
        if len(stack) > 0:
            return False
        return True
            