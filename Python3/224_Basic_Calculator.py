class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            self.operation(stack)
            if s[i] in '()+-':
                stack.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
            else:
                number = []
                while i < len(s) and s[i].isdigit():
                    number.append(s[i])
                    i += 1
                stack.append(int(''.join(number)))
        self.operation(stack)
        return stack[0]

    def operation(self, stack):
    	if len(stack) >= 3:   # can apply + -
    		if type(stack[-3]) == type(stack[-1]):
    			if stack[-2] == '+':
    				stack[-3] = stack[-3] + stack[-1]
    				del stack[-2:]
    				return self.operation(stack)
    			elif stack[-2] == '-':
    				stack[-3] = stack[-3] - stack[-1]
    				del stack[-2:]
    				return self.operation(stack)
    		if stack[-3] == '(' and stack[-1] == ')':
    			stack[-3] = stack[-2]
    			del stack[-2:]
    			return self.operation(stack)

so = Solution()
so.calculate('(1+(4+5+2)-3)+(6+8)')
