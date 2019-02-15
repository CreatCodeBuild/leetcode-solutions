/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    iQ := iterator(p)
    iP := iterator(q)
    
    for vQ := range iQ {
        vP := <- iP
        if vQ == nil && vP != nil {
            return false
        }
        if vQ != nil && vP == nil {
            return false
        }
        if vQ != nil && vP != nil {
            if vQ.Val != vP.Val {
                return false
            }
        }  
    }
    return true
}


// iterator（迭代器）, iterable（可迭代的数据）, generator（生成器）
// generator 是一种特殊的 iterable
// iterator 是用来 iterate 一个 iterable 的工具

func iterator(n *TreeNode) chan *TreeNode {
    
    c := make(chan *TreeNode)
    go func() {
        c <- n
        if n != nil {
            for n := range iterator(n.Left) {
                c <- n
            }
            for n := range iterator(n.Right) {
                c <- n
            }
        }
        close(c)
    }()
    return c
}
