class Solution(object):
    def evalRPN(self, tokens):
        from math import floor, ceil
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [0] * len(tokens)
        i = -1
        for token in tokens:
            i -= 1
            if token == '+':
                stack[i] = stack[i] + stack[i+1]
            elif token == '-':
                stack[i] = stack[i] - stack[i+1]
            elif token == '*':
                stack[i] = stack[i] * stack[i+1]
            elif token == '/':
                stack[i] = int(stack[i] / float(stack[i+1]))
            else:
                i += 2
                stack[i] = int(token)
        return stack[0]

# Beat 100%
