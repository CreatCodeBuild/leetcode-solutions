// https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/
func singleNonDuplicate(nums []int) int {
    // [8]
    if len(nums) == 1 {
        return nums[0]
    }
    m := len(nums) / 2
    // [3,3,7,7,8,9,9,11,11]
    //         8
    if nums[m] != nums[m-1] && nums[m] != nums[m+1] {
        return nums[m]
    } else if nums[m] == nums[m-1] {
        if m % 2 == 0 {
            // [1,1,2,3,3,4,4,8,8]
            //  0 1 2 3 4 5 6 7 8
            return singleNonDuplicate(nums[:m-1])
        } else {
            // [3,3,7,7,10,11,11]
            //  0 1 2 3 4  5  6
            return singleNonDuplicate(nums[m+1:])
        }
    } else { // if nums[m] == nums[m+1]
        if m % 2 == 0 {
            // [1,1,3,3,7,7,10,11,11]
            //  0 1 2 3 4 5 6  7  8
            return singleNonDuplicate(nums[m+2:])
        } else {
            // [1,1,2,3,3,4,4,5,5,8,8]
            //  0 1 2 3 4 5 6 7 8 9 10
            return singleNonDuplicate(nums[:m])
        }
    }
}
