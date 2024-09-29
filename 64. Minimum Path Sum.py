class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # find the min of each element depending on its top or left and sum with current element
        rows = len(grid)
        cols = len(grid[0])

        # initialize top and left edges
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
        