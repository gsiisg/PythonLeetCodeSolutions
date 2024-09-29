class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        possible = {}

        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                # print(row,col)
                if (row == n-1) or (col == m-1):
                    possible[(row,col)] = 1
                    continue
                else:
                    possible[(row,col)] = possible[(row+1,col)] + possible[(row,col+1)]

                # print(row,col, possible[(row,col)])
        
        return possible[(0,0)]