# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#
# Constraints:
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400


# Almost identical to my 2024-09-09 attempt
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         length = len(nums)
#         if not nums:
#             return 0
#         if length==1:
#             return nums[0]
#         if length==2:
#             return max(nums[0],nums[1])

#         # use the original array to store the max possible at each index
#         # start from the 3rd index, all previous elements are the max possible at an index
#         # need to take care of index 2 independently
#         nums[2] += nums[0]
#         for i in range(3, length):
#             # for every index, it can sum the max from 1 index away (i-2) or 2 index away (i-3)
#             nums[i] = (max(nums[i]+nums[i-2], nums[i]+nums[i-3]))

#         # the max could be the last or the 2nd to the last in the original array
#         return max(nums[-1],nums[-2])

# quickest solution, don't understand it yet
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         e = i = 0
#         for x in nums:
#             e, i = i, max(e +x, i)
#         return max(e,i)

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length==1:
            return nums[0]
        elif length==2:
            return max(nums)
        elif length==3:
            nums[2] = nums[0]+nums[2]
            return max(nums[1],nums[2])

        # for each element after the 2nd
        # the value set to the total if that step is used
        # don't worry about the step of an element skipped, just don't record on it
        # at the end pick the max of last two, because the 2nd to last will have last element skipped
        nums[2] = nums[0]+nums[2]

        for i in range(3, length):
            nums[i] = nums[i]+max(nums[i-2], nums[i-3])

        return max(nums[-1],nums[-2])