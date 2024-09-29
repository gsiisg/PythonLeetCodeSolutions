class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # Took too long, Time Limit Exceeded, 99/106 passed
        # # Brute force try all possibilities with early stop

        # def recursiveTry(s1, s2, s3):

        #     if not s1:
        #         return s2 == s3
        #     if not s2:
        #         return s1 == s3

        #     if s1[0] == s2[0] == s3[0]:
        #         return recursiveTry(s1[1:], s2, s3[1:]) or recursiveTry(s1, s2[1:], s3[1:])
        #     elif s1[0] == s3[0]:
        #         return recursiveTry(s1[1:], s2, s3[1:])
        #     elif s2[0] == s3[0]:
        #         return recursiveTry(s1, s2[1:], s3[1:])

        # return recursiveTry(s1, s2, s3)



        # https://leetcode.com/problems/interleaving-string/solutions/3956393/99-78-2-approaches-dp-recursion/
        # this is same as my method above but keeping track of i,j,k index helps record which (i,j) pair are false
        # memo the false (i,j) pair will speed up calc enough to pass test cases

        # m, n, l = len(s1), len(s2), len(s3)
        # if m + n != l:
        #     return False
        
        # memo = {} 
        
        # def helper(i: int, j: int, k: int) -> bool:
        #     if k == l:
        #         return True
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     ans = False
        #     if i < m and s1[i] == s3[k]:
        #         ans = ans or helper(i + 1, j, k + 1)
                
        #     if j < n and s2[j] == s3[k]:
        #         ans = ans or helper(i, j + 1, k + 1)
            
        #     memo[(i, j)] = ans

        #     return ans
        
        # return helper(0, 0, 0)



        # My recursion method + memo, passed
        # if s1 == s2 == s3 == '':
        #     return True

        # if len(s1) + len(s2) != len(s3):
        #     return False

        # memo = {}

        # def recursiveTry(s1, s2, s3):

        #     if (s1,s2) in memo:
        #         return memo[(s1,s2)]

        #     if not s1:
        #         ans = s2 == s3
        #         memo[(s1,s2)] = ans
        #         return ans
        #     if not s2:
        #         ans = s1 == s3
        #         memo[(s1,s2)] = ans
        #         return ans

        #     if s1[0] == s2[0] == s3[0]:
        #         ans1 = recursiveTry(s1[1:], s2, s3[1:]) 
        #         ans2 = recursiveTry(s1, s2[1:], s3[1:])
        #         memo[(s1[1:], s2)] = ans1
        #         memo[(s1, s2[1:])] = ans2
        #         return ans1 or ans2
        #     elif s1[0] == s3[0]:
        #         ans = recursiveTry(s1[1:], s2, s3[1:])
        #         memo[(s1[1:], s2)] = ans
        #         return ans
        #     elif s2[0] == s3[0]:
        #         ans = recursiveTry(s1, s2[1:], s3[1:])
        #         memo[(s1, s2[1:])] = ans
        #         return ans

        # return recursiveTry(s1, s2, s3)




        # # 2D dynamic programming, passed
        # l1, l2, l3 = len(s1), len(s2), len(s3)

        # # early stopping cases
        # if l1 + l2 != l3:
        #     return False

        # if s1==s2==s3=='':
        #     return True

        # if not s1:
        #     return s2 == s3
        
        # if not s2:
        #     return s1 == s3

        # # create table to store intermediate results, l1 rows and l2 columns
        # table = [[0] * (l2 + 1) for x in range(l1 + 1)]

        # table[0][0] = True

        # # each edge element only depend on the previous result and the letter of s3 matching with s1 or s2
        # for i in range(1,l1+1):
        #     table[i][0] = table[i-1][0] and s1[i-1]==s3[i-1]

        # for j in range(1,l2+1):
        #     table[0][j] = table[0][j-1] and s2[j-1]==s3[j-1]

        # # each non edge element can depend on the top or left element and corresponding letter in s3
        # for i in range(1,l1+1):
        #     for j in range(1,l2+1):
        #         table[i][j] = (table[i-1][j] and s1[i-1] == s3[i + j - 1]) or (table[i][j-1] and s2[j-1] == s3[i + j - 1])

        # return table[l1][l2]



        # 1D dynamic programming
        l1, l2, l3 = len(s1), len(s2), len(s3)

        # early stopping cases
        if l1 + l2 != l3:
            return False

        if s1==s2==s3=='':
            return True

        if not s1:
            return s2 == s3
        
        if not s2:
            return s1 == s3

        # since we need to know only 1 additional row at any given time, we want to minimize the number of columns per row
        # if number of columns is creater than number of rows, swap the two strings
        # this is to optimize for space to be O(min(l1,l2))
        # at any given time only need to know one column's worth of data, so make sure column is the smaller of the two
        if l1 < l2:
            s1,s2,l1,l2 = s2,s1,l2,l1

        # initialize table
        table = [False] * (l2 + 1)
        table[0] = True # when empty

        # handle the edge cases like the 2D case
        for j in range(1,l2 + 1):
            table[j] = table[j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(1, l1 + 1):
            table[0] = table[0] and s1[i - 1] == s3[i - 1] # for each iteration of i re-initialize starting element
            for j in range(1, l2 + 1):
                # 2D case: 
                # table[i][j] = (table[i-1][j] and s1[i-1] == s3[i + j - 1]) or (table[i][j-1] and s2[j-1] == s3[i + j - 1])
                # 1D case:
                # - replace table[i][j] with just table[j]
                # - replace table[i-1][j] with just table[j]
                # - replace table[i][j-1] with just table[j-1]
                table[j] = (table[j] and s1[i - 1] == s3[i + j -1]) or (table[j - 1] and s2[j - 1] == s3[i + j - 1])

        return table[l2]
        




        