/**
https://leetcode.com/problems/range-sum-of-bst
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, L int, R int) int {
    
    sum := 0
    
    if root.Val >= L && root.Val <= R {
        sum += root.Val
    }
    
    if root.Val > L && root.Left != nil {
        sum += rangeSumBST(root.Left, L, R)
    }
    
    if root.Val < R && root.Right != nil {
        sum += rangeSumBST(root.Right, L, R)
    }
    
    return sum
    
}
