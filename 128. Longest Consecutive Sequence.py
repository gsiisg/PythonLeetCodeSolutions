#!/usr/bin/env python
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use set(nums) is faster than storing each number in a dictionary to
        # and use 'for i in d' to check without duplicates
        d = set(nums)
        longest = 0
        for i in d:
            # if i-1 is not in d means it is the beginning of a streak
            if i-1 not in d:
                # set the next number in the streak to current number i + 1
                nextNum = i + 1
                # loop until next number is no longer found
                while nextNum in d:
                    nextNum += 1
                # update longest to the end of the streak (nextNum) subtract current i
                longest = max(longest, nextNum-i)
        return longest

# O(n) 35 ms
