#!/usr/bin/env python
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): # delete those useless elements that is negative or outside the range from 1 to n
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): # use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0: # if the number divided by n floored is 0, that means the i-th element has not been accounted for since it did not get +=n added, so return i
                return i
        return n

# O(n) 33 ms
