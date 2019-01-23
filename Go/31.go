// https://leetcode.com/problems/next-permutation/
import "sort"

func nextPermutation(nums []int)  {
    for i := len(nums)-1; i >= 1; i-- {
        if nums[i] > nums[i-1] {
            for j := len(nums)-1; j > i-1; j-- {     
                if nums[j] > nums[i-1] {
                    s := sort.IntSlice(nums)
                    s.Swap(j, i-1)
                    reverse(nums, i, len(nums)-1)
                    return                
                } 
            }  
        }    
    }
    reverse(nums, 0, len(nums)-1)
}

func reverse(nums sort.IntSlice, i, j int) {
    for x := 0; x <= (j-i) / 2; x++ {        
        nums.Swap(i+x, j-x)
    }
}
