Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # This is Kadane's Algorithm
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = float('-inf'), 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max

# This is faster than Kadane's Algo   
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num

            best_sum = max(best_sum, current_sum)

        return best_sum