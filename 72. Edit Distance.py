# https://leetcode.com/problems/edit-distance/solutions/4749519/fastest-python-code-with-straightforward-visual-explanation/
#          +r      +o       +s
#     horse  rhorse  rohorse  roshorse
# -h       ↘️ 1
#     orse   rorse   roorse   rosorse
# -o               ↘️ 0
#     rse    rrse    rorse    rosrse
# -r                  ⬇️ 1   
#     se     rs      rose     rosse
# -s                        ↘️ 0
#     e      r       roe      rose
# -e                          ⬇️ 1
#     ""     r       ro       ros

# movig diagonally in this diagram produces the least number of moves needed (could be 0 or 1)
# by moving down or to the right (always a 1), this incurrs more overall steps


# https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)

        # if the letters are same, no op required
        # the rest get it from the min of the 3 possible neighbors left, diag left top, top
        # 1) going down the row is delete from word1
        # 2) going right the col is insert into word1
        # 3) going diag down+right is replacing from word1
        # edge cases of left and top edges are only either delete or insert

        # originally thought if I rearrange word1 and 2 can always use insert with no delete
        # this cannot be done if we want to minimize changes needed

        # initialize 0 table to store values
        # table = [[0] * (n + 1)] * (m + 1) # CANNOT do this, the array rows are copies of each other, 
        # change one change them all
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            table[i][0] = i # number of deletes from word1
            # print('at i=',i)
            # print(table)

        for j in range(1, n + 1):
            table[0][j] = j # number of inserts into word1

        # print(table)

        # if we go along the edges we'd add word2 then delete word1 or delete word1 then add word2
        # taking a step on the edges is always 1 operation per step
        # the shortest path is take diagonal whenever possible resulting in 0 or 1 operation per step
        # 0 when nothing needs to be changed

        # iterate over all elements
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    replace = table[i - 1][j - 1]
                    delete = table[i - 1][j]
                    insert = table[i][j - 1]
                    table[i][j] = min(replace, delete, insert) + 1

        return table[m][n]