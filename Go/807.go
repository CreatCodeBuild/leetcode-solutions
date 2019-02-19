// https://leetcode.com/problems/max-increase-to-keep-city-skyline/
func maxIncreaseKeepingSkyline(grid [][]int) int {
    row_maxs := make([]int, len(grid))    
    col_maxs := make([]int, len(grid[0]))
    for j := range grid[0] {
        col_maxs[j] = grid[0][j]
        for i := range grid {
            if grid[i][j] > col_maxs[j] {
                col_maxs[j] = grid[i][j]
            }
        }
    }
    sum := 0
    for i, row := range grid {
        row_maxs[i] = max(row) 
        for j, num := range row {     
            min := 0
            if row_maxs[i] > col_maxs[j] {
                min = col_maxs[j]
            } else {
                min = row_maxs[i]
            }      
            sum += min - num 
        }
    }
    return sum
}

func max(slice []int) int {
    m := slice[0]
    for _, num := range slice {
        if num > m {
            m = num
        }
    }
    return m
}
