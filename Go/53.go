package main

import "fmt"

func main() {
	data := []int{-2,1,-3,4,-1,2,1,-5,4}
	sum, s, e := maxSubArray(data)
	fmt.Println(sum, data[s:e+1])
}

func maxSubArray(nums []int) (int, int, int) {
    max := nums[0]
    cutting_point := nums[0]
    s := 0
    e := 0
    
    for i := 1; i < len(nums); i++ {
        
        if doesDecrease(cutting_point) {
            cutting_point = 0
            s = i
        }
        
        cutting_point = cutting_point + nums[i]
        if cutting_point > max {
            max = cutting_point
            e = i
        }  
    }
    return max, s, e
}

func doesDecrease(num int) bool {
    return num < 0
}
