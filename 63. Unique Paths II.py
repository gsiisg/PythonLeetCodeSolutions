class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # possible = {}
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # # early stop
        # if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        #     return 0

        # for row in range(m-1, -1, -1):
        #     for col in range(n-1, -1, -1):
        #         # print(row,col)
        #         if obstacleGrid[row][col] == 1:
        #             possible[(row,col)] = 0
        #         elif row == m-1 and col == n-1: # this is the destination
        #             possible[(row,col)] = 1
        #         elif (row == m-1): # on the last row
        #             if possible[(row,col+1)] != 0:
        #                 possible[(row,col)] = 1
        #             else:
        #                 possible[(row,col)] = 0
        #         elif (col == n-1): # on last col
        #             if possible[(row+1,col)] != 0:
        #                 possible[(row,col)] = 1
        #             else:
        #                 possible[(row,col)] = 0
        #         else:
        #             possible[(row,col)] = possible[(row+1,col)] + possible[(row,col+1)]
        
        # return possible[(0,0)]


        # simplified
        paths = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if obstacleGrid[row][col] == 1: # if obstacle then 0
                    paths[(row,col)] = 0
                elif (row==rows-1) and (col == cols-1): # if exit then it is set to 1
                    paths[(row,col)] = 1
                elif row==rows-1: # lower edge depends only on values to right
                    paths[(row,col)] = paths[(row,col+1)]
                elif col==cols-1: # right edge depends only on values to bottom
                    paths[(row,col)] = paths[(row+1,col)]
                else:
                    paths[(row,col)] = paths[row+1,col]+paths[row,col+1] # depends on two neighbors to right and bottom only

        return paths[(0,0)]