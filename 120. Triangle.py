class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # Time Limit Exceeded 42/45
        # last_row = len(triangle) - 1
        # def calcSum(row, index, triangle, total):
        #     if row == last_row:
        #         return total
        #     left_total = total + triangle[row+1][index]
        #     right_total = total + triangle[row+1][index+1]
        #     return min(calcSum(row+1, index, triangle, left_total), calcSum(row+1, index+1, triangle, right_total))

        # min_sum = calcSum(0,0,triangle, triangle[0][0])

        # return min_sum



        # # use the min total of 2 from earlier row to pair with current row
        # row_nums = len(triangle)-1
        # prev_row = triangle[row_nums]
        # for row in range(row_nums-1,-1,-1):
        #     curr_row = []
        #     # print(f'on row {row}')
        #     for i in range(len(triangle[row])):
        #         curr_row.append(triangle[row][i] + min(prev_row[i],prev_row[i+1]))
        #     # print(f'min sum is {curr_row}')
        #     prev_row = curr_row

        # return prev_row[0]



        # simplified
        num_rows = len(triangle)
        for row in range(num_rows-2,-1,-1):
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])

        return triangle[0][0] 