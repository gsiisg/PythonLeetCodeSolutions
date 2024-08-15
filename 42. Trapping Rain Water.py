#!/usr/bin/env python
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0 # cannot trap rain water with less than 3 cells
        left, right = 0, len(height) - 1
        water = 0
        maxleft, maxright = height[left], height[right]
        while left < right: # while the two indices do not cross
            if maxleft < maxright: # if the maxright is higher, left side can continue to increment and trap rain water below maxleft
                water += maxleft - height[left]
                left += 1
                maxleft = max(maxleft, height[left]) # after trapping rain, update maxleft
            else: # if maxleft is higher, right side can continue to decrement and trap rain water below maxright
                water += maxright - height[right]
                right -= 1
                maxright = max(maxright, height[right]) # after trapping rain, update maxright
        return water

# O(n) 42 ms

