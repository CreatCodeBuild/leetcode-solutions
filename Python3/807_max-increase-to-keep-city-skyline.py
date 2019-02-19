# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        total = 0
        
        l = len(grid)
        w = len(grid[0])
        
        row_maxs = [max(row) for row in grid]
        col_maxs = [max(get_col(grid, j)) for j in range(w)]
        
        for i in range(l):
            for j in range(w):
                total += min(row_maxs[i], col_maxs[j]) - grid[i][j]
                
        return total

# column
def get_col(grid, j):
    l = [0] * len(grid[0]) 
    for i, row in enumerate(grid):
        l[i] = row[j]
    return l
