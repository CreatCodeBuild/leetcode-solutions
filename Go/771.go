import "strings"

func numJewelsInStones(J string, S string) int {
    set := make(map[rune]struct{})
    for _, letter := range J {
        set[letter] = struct{}{}
    }
    
    c := 0
    for _, letter := range S {
        if _, ok := set[letter]; ok {
            c += 1
        }
    }
    return c
    // time: O(n)
    // space: O(m)
}
