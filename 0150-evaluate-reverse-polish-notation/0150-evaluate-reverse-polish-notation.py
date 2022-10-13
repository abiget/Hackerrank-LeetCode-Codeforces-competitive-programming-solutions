import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i,j = 0, len(tokens)
        stack = []
        op = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        while i < j:
            if tokens[i] not in op.keys():
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                stack.append(int(op[tokens[i]](second,first)))
            i += 1
        return stack[0]