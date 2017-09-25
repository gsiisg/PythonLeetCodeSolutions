#!/usr/bin/env python
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        return self.findkth(nums1, nums2, l//2) if l%2 else (self.findkth(nums1, nums2, l//2-1) + self.findkth(nums1, nums2, l//2))/2.0 # if odd return mid, else average of two mids

    def findkth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A # ensure that A is always smaller of the two
        if not A:
            return B[k] # if nothing in A return kth in B
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1]) # if k is last element return the max of last elements
        i = len(A)//2 # for general findkth usually this is k//2 and it could be larger than len(A), but for median this is OK
        j = k - i # for median, k - i with lenA<lenB this is never negative, not true in general
        if A[i] < B[j]:
            return self.findkth(A[i:], B[:j], j) # when looking for kth smallest, i elements removed from k (from front of A), so the new k is k - i = j
        else:
            return self.findkth(A[:i], B[j:], i) # when looking for kth smallest, j elements removed from k (from front of B), so the new k is k - j = i

# O(log(min(m, n))) 85 ms
