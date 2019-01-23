"""
https://leetcode.com/problems/next-permutation/

1,2,3,6,5,4,7
1,2,3,6,5,7,4
1,2,3,6,7,4,5
1,2,3,6,7,5,4
1,2,3,7,4,5,6
1,2,3,7,4,6,5
1,2,3,7,5,4,6
1,2,3,7,5,6,4
1,2,4,3,5,6,7
"""
class Solution:
    def nextPermutation(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        nums[i:] = list(reversed(nums[i:]))
                        return
        for i in range(len(nums)//2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]
