#!/usr/bin/env python
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        length = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: # skip if the num is already done, avoid duplicates
                continue
            l = i + 1 # set l and r pointers to the next and last num respectively
            r = length - 1
            while l < r:
                ans = num + nums[l] + nums[r]
                if ans == 0:
                    results.append((num, nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]: # skip repeating num on the left
                        l += 1
                    l += 1
                    while l < r and nums[r] ==nums[r - 1]: # skip repeating num on the right
                        r -= 1
                    r -= 1
                elif ans > 0: # if ans is too large, decrease the r pointer
                    r -= 1
                elif ans < 0: # if ans is too small, increase the l pointer
                    l += 1
        return results

# O(n^2) 952 ms
