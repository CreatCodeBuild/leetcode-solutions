/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isUnivalTree(root *TreeNode) bool {
    if root == nil {
        return true
    }
    
    this := true
    lv := root.Val
    rv := root.Val
    if root.Left != nil {
        lv = root.Left.Val
    }
    if root.Right != nil {
        rv = root.Right.Val
    }
    
    this = (root.Val == lv) && (root.Val == rv)
    return isUnivalTree(root.Left) && isUnivalTree(root.Right) && this
}
