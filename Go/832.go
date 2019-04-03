func flipAndInvertImage(A [][]int) [][]int {
    for _, row := range A {
        for i := len(row)/2-1; i >= 0; i-- {
            opp := len(row)-1-i
            row[i], row[opp] = row[opp], row[i]
        }
        for j, ele := range row {
            row[j] = 1 - ele
        }
    }
    return A
}
