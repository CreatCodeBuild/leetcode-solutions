/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func constructMaximumBinaryTree(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil
    }
    
    maxI := 0
    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[maxI] {
            maxI = i
        }
    }
    
    root := TreeNode{Val: nums[maxI]}
    
    root.Left = constructMaximumBinaryTree(nums[:maxI])
    root.Right = constructMaximumBinaryTree(nums[maxI+1:])
    
    return &root
}
