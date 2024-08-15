# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        stack = []
        max_area = 0
        curr_index = 0
        while curr_index < len(heights):
            if not stack or (heights[stack[-1]] < heights[curr_index]):
                # remember the index that is greater than the height of the last index in stack
                stack.append(curr_index)
                curr_index += 1
            else:
                # when the height of index is smaller than the height of the last index in stack
                # remove the index from top_of_stack and using index to last index in stack as the width
                # using last index in stack as left edge and current index as right edge
                # will ensure non sequential indices in stack that were already taken out is accounted for
                top_of_stack = stack.pop()
                # if stack is empty use current index as width
                # since there's nothing in stack that is less than current height at top_of_stack
                width = curr_index - 1 - stack[-1] if stack else curr_index
                area = heights[top_of_stack] * width
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            # if stack is empty use current index as width
            # since there's nothing in stack that is less than current height at top_of_stack
            width = curr_index - 1 - stack[-1] if stack else curr_index
            area = heights[top_of_stack] * width
            max_area = max(max_area, area)

        return max_area