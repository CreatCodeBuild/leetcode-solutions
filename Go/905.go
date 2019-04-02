// Solution 1, ordered
func sortArrayByParity(A []int) []int {
    even := []int{}
    odd := []int{}
    
    for _, n := range A {
        if n % 2 == 0 {
            even = append(even, n)
        } else {
            odd = append(odd, n)
        }
    }
    
    ret := make([]int, len(even) + len(odd))
    for i, n := range even {
        ret[i] = n
    }
    for i, n := range odd {
        ret[i+len(even)] = n
    }
    
    return ret
}

// Solution 2, odds reversed
func sortArrayByParity(A []int) []int {
    
    ret := make([]int, len(A), len(A))
    
    i := 0  // even
    j := 1  // odd
    for _, n := range A {
        if n % 2 == 0 {
            ret[i] = n
            i++
        } else {
            ret[len(A)-j] = n
            j++
        }
    }
    
    return ret
}
