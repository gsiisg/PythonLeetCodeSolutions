#!/usr/bin/env python
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        if l < 3:
            return l
        maxpts = 0
        for i in range(l-1): # don't need the last element in initial loop
            overlap = 0
            pi = points[i]
            ptdict = {None: 1} # set some dummy element so that when ptdict is empty it will return at least the initial point of 1 as max
            xi, yi = pi.x, pi.y
            for j in range(i + 1, l):
                pf = points[j]
                xf, yf = pf.x, pf.y
                if xi == xf and yi == yf: # when the point overlap with the current point, increase overlap counter, this will in effect add to all points in ptdict
                    overlap += 1
                    continue
                if xi == xf: # when slope is infinity
                    slope = 'i'
                else:
                    dx, dy = xf - xi, yf - yi
                    gcd = self.getGcd(dx, dy) # use gcd or need to import numpy as np.longdouble which is more time consuming for high accuracy fractions
                    dx //= gcd # reduce the fraction by its greatest common denominator
                    dy //= gcd
                    slope = (dx, dy) # so that the slope can be expressed by two integers
                if slope not in ptdict: # when slope is not already in ptdict, add one, will represent the initial point along this slope
                    ptdict[slope] = 1
                ptdict[slope] += 1
            maxpts = max(maxpts, max(ptdict.values()) + overlap)
        return maxpts

    def getGcd(self, dx, dy): # cleaver way to recursively return greatest common denominator
        if dy == 0: return dx
        else: return self.getGcd(dy, dx % dy)
