# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [8]
        if len(nums) == 1:
            return nums[0]
        
        
        m = len(nums) // 2
        # [3,3,7,7,8,9,9,11,11]
        #          8
        if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
            return nums[m]
        
        if nums[m] == nums[m-1]:
            if m % 2 == 0:
                # [1,1,2,3,3,4,4,8,8]
                #  0 1 2 3 4 5 6 7 8
                return self.singleNonDuplicate(nums[:m-1])

            else:
                # [3,3,7,7,10,11,11]
                #  0 1 2 3 4  5  6
                return self.singleNonDuplicate(nums[m+1:])
            
        if nums[m] == nums[m+1]:
            if m % 2 == 0:
                # [1,1,3,3,7,7,10,11,11]
                #  0 1 2 3 4 5 6  7  8
                return self.singleNonDuplicate(nums[m+2:])

            else:
                # [1,1,2,3,3,4,4,5,5,8,8]
                #  0 1 2 3 4 5 6 7 8 9 10
                return self.singleNonDuplicate(nums[:m])
