#!/usr/bin/env python
"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        if not root:
            return 0
        self.curr_max = -float('inf') # initialize the variable to be kept updated as smallest number
        return max(self.maxPathSumH(root), self.curr_max) # the self.maxPathSumH() MUST come before self.curr_max, because curr_max gets updated in the maxPathSumH()

    def maxPathSumH(self, root):
        if not root:
            return -float('inf')
            # set to most negative (-float('inf')) to prevent this path from even being considered, since it is None
            # if path is set to 0 or a negative number it will mess up the max() later, so must set to -float('inf')
        left = self.maxPathSumH(root.left)
        right = self.maxPathSumH(root.right)
        self.curr_max = max(self.curr_max, left, right, left + root.val + right) # find curr_max from 4 sources: curr_max, left, right, left+root+right
        return max(root.val, root.val + left, root.val + right) # return the connected pieces max (root+left, root+right) or just root
