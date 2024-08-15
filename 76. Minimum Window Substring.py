#!/usr/bin/env python
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # takes care of edge case when t is longer than s
        if len(t) > len(s):
            return ""

        # initialize dictionary to store letters needed and counted as [#needed, #counted]
        needcount = {}
        # initialize the variable to keep track of number of letters still needed
        needNum = 0
        for letter in t:
            # sets default to [0,0] if letter not already in dictionary
            needcount[letter] = needcount.get(letter,[0,0])
            # needed letter goes in slot 0 from 't', count will go in slot 1 later when looping through 's'
            needcount[letter][0] += 1
            needNum += 1

        # initialize indices and counters
        left, right = 0, 0
        length = len(s)
        minlen = length+1

        # stop condition is when right exceeds the length and when needNum is 0
        while right < length or not needNum:
            # while there is needNum indicating missing letters, increase right
            if needNum:
                letter = s[right]
                right += 1
                if letter in t:
                    # calculate how many of this particular letter are missing by need-count
                    if needcount[letter][0]-needcount[letter][1] > 0:
                        # if any missing, subtract 1 from needNum because we just adding 1 of this letter
                        needNum -= 1
                    # increment the letter count by 1 since we just added this letter
                    needcount[letter][1] += 1

            # while there is no needNum when all letters are fulfilled and left < right, increase left
            elif not needNum and left < right:
                letter = s[left]
                left += 1
                if letter in t:
                    # calculate how many of this particular letter are missing by need-count
                    if needcount[letter][0]-needcount[letter][1] >= 0:
                        # if there any are missing or need is same as count, then add 1 to needNum
                        # because 1 was just gotten rid of when left moved up by one
                        needNum += 1
                    # update count accordingly
                    needcount[letter][1] -= 1

            # after each move of left or right, check if the new window is smaller than minlen
            if not needNum:
                if right-left < minlen:
                    # if right-left is smaller then update minlen and the start, end indices
                    minlen = right-left
                    start, end = left, right

        # return the string starting and ending at the specified indices if minlen has been modified
        return s[start:end] if minlen < len(s)+1 else ""

# O(n) 145 ms
