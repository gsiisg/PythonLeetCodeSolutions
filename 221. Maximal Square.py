class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # Adjusted to match my accepted submission back in Feb 15, 2021
        # rows = len(matrix)
        # cols = len(matrix[0])

        # # Creating table takes additional mem/time, use original matrix to store results
        # for i in range(rows):
        #     row_total = 0
        #     for j in range(cols):
        #         if matrix[i][j] == '0':
        #             row_total = 0
        #         row_total += int(matrix[i][j])
        #         matrix[i][j] = row_total

        # # find number of consecutive elements to see if it match the number in table for square
        # # find the max over each of the column slice to determine the max square

        # max_side = int(matrix[0][0])

        # for i in range(rows):
        #     # print('parsing rows')
        #     # early stop, remaining column slices cannot form squares larger than current max_side
        #     if i + max_side > rows - 1:
        #         continue

        #     for j in range(cols):
        #         check_side = matrix[i][j]
        #         # print(f'parsing cols, on {i},{j}, with max_side {max_side} check_side {check_side}')
        #         if check_side > max_side:
        #             # print(f'at {i},{j} check side {check_side}, max_side {max_side}')
        #             # check each column slice element to see if condition satisfied
        #             curr_min = float('inf')
        #             # print(f'checking k range ({i},{i+check_side})')
        #             for curr in range(check_side):
        #             #     # print(f'checking {k},{j}')
        #             #     # check if all elements are >= check_side
        #             #     # check number of consecutive elements starting from i,j
        #             #     if k < rows and table[k][j] != 0:
        #             #         col_slice.append(table[k][j])
        #             #     else:
        #             #         # if there's a break in the consecutiveness then end there
        #             #         break
        #             # print(f'col_slice {col_slice}')
        #             # ***************FLAWED LOGIC*****************
        #             # col_min = min(col_slice)
        #             # col_min = min(col_min, len(col_slice))
        #             # max_side = max(max_side, col_min)
        #             # print(f'max_side {max_side}')

        #                 if i + curr < rows:
        #                     curr_min = min(curr_min, matrix[i + curr][j])
        #                     if curr_min == curr + 1:
        #                         # this means the side matches check_side exactly
        #                         break
        #                     elif curr_min < curr + 1:
        #                         # this means the match didn't happen for check_side, only a value smaller is available
        #                         curr -= 1
        #                         break
        #                 else:
        #                     # index exceeded number of rows available
        #                     curr -= 1
        #                     break

        #             max_side = max(max_side, curr+1)


        # return max_side * max_side

        

        rows = len(matrix)
        cols = len(matrix[0])

        max_side = int(matrix[0][0])

        for i in range(rows):
            for j in range(cols):
                # print(f'on {i},{j}')
                # set left
                if j == 0:
                    left = 0
                else:
                    left = matrix[i][j-1]

                # set top
                if i == 0:
                    top = 0
                else:
                    top = matrix[i-1][j]

                # set diag
                if i == 0 or j == 0:
                    diag = 0
                else:
                    diag = matrix[i-1][j-1]

                # set new value
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                    curr_max = 0
                else:
                    curr_max = 1 + min(left, top, diag)
                    matrix[i][j] = curr_max

                max_side = max(max_side, curr_max)
                # print(f'matrix now', matrix)

        return max_side**2




