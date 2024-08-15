#!/usr/bin/env python
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        letterdict = {} # to record a letter's previous position when it was last encountered
        maxlen = 0
        start = 0
        for i, letter in enumerate(s):
            if letter in letterdict and start <= letterdict[letter]: # if the letter appeared before and is in a position after the start change the new start to after the appeared letter
                start = letterdict[letter] + 1 # when a letter appeared again within the length of current substring, change the start to right after the appearance of the letter
            else:
                maxlen = max(maxlen, i - start + 1) # calculate the new max length if the new letter has not been encountered before or not within the substring from start to i
            letterdict[letter] = i # record the position of this letter
        return maxlen

# O(n) 75 ms

