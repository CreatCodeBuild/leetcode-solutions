# https://leetcode.com/problems/maximum-subarray/
# faster than 100%

class Solution1:

    def maxSubArray(self, a):
        """
        just the sum
        """

        max_so_far = a[0]
        max_ending_here = a[0]

        for i in range(1, len(a)):
            if max_ending_here < 0: 
                max_ending_here = 0
            
            max_ending_here = max_ending_here + a[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

        return max_so_far

    def max_subarray(self, a):
        """
        the sum and the subarray index
        """
        max_so_far = a[0]
        max_ending_here = a[0]
        s = 0
        e = 0 

        for i in range(1, len(a)):

            if max_ending_here < 0: 
                max_ending_here = 0
                s = i
            
            max_ending_here = max_ending_here + a[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                e = i

        return max_so_far, s, e


data = [-1, 2,1]
print(Solution1().max_subarray(data))
