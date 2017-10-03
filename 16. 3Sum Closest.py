#!/usr/bin/env python
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        diff = float('inf') # delta difference between the total of the 3 numbers and the target, initialize to infinity
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: # skip numbers that were done already similar to 3Sum
                continue
            l = i + 1 # initialize the left, right pointer to the right of i-th and last index
            r = length - 1
            while l < r:
                total = num + nums[l] + nums[r] # calculate the total of the 3 numbers
                if total == target: # if the total same as target return total
                    return total
                if abs(total-target) < diff: # if the abs diff between total and target is smaller than diff, set as the new diff and set total as the new result
                    diff = abs(total - target)
                    result = total
                if total > target: # if total is too large decrease right pointer
                    r -= 1
                elif total < target: # if total is too small increase left pointer
                    l += 1
        return result

# O(n^2) 99 ms
