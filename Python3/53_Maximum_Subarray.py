# https://leetcode.com/problems/maximum-subarray/

class Solution1:

    def maxSubArray(self, a): 
        
        max_so_far = a[0]
        max_ending_here = a[0] if a[0] > 0 else 0

        for i in range(1, len(a)):
            
            max_ending_here = max_ending_here + a[i]
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
    
            if max_ending_here < 0: 
                max_ending_here = 0

        return max_so_far 


data = [-1, 2,1]
print(Solution1().maxSubArray(data))
