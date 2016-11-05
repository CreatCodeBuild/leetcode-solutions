# recursion, slow
class Solution(object):
    def __init__(self):
        self.way = 0
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # check slice 1
        if len(s) >= 2 and 10 <= int(s[0:2]) <= 26:
            slice = s[2:]
            if len(slice) == 0:
                self.way += 1
            else:
                self.numDecodings(slice)

        # check slice 2
        if len(s) >= 1 and 1 <= int(s[0]):
            slice = s[1:]
            if len(slice) == 0:
                self.way += 1
            else:
                self.numDecodings(slice)
        return self.way

# dp, quick, but kind of magic to me
class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if s:
			T = [0] * (len(s) + 1)
			T[0] = 1
			T[1] = 1 if s[0] != '0' else 0
			for i in range(2, len(s)+1):
				if int(s[i-1:i]) >= 1:
					T[i] += T[i-1]
				if 10 <= int(s[i-2:i]) <= 26:
					T[i] += T[i-2]
			return T[-1]
		else:
			return 0

so = Solution()
r = so.numDecodings('4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948')
print(r)
