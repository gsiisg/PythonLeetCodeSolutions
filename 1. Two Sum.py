#!/usr/bin/env python
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,n in enumerate(nums): # go through all elements
            if target - n in d: # if the complement of target is already in the dictionary for n
                return [d[target - n], i] # then return the index stored in dictionary and current index i
            else:
                d[n] = i # or else add the number to dictionary with current index i

Solution().twoSum([2, 7, 11, 15], 9)
# time: O(n) 32 ms 97.90%
