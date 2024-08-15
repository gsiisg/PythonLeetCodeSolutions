#!/usr/bin/env python
"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if s==s[::-1]:
            return s
        zero_pos = []
        cur_sum = 0
        cur_sum_cubued = 0
        for i in range(1, len(s)):
            # calculate the number difference between ascii characters
            diff = ord(s[i]) - ord(s[i-1])
            cur_sum += diff
            cur_sum_cubued += diff**3
            # if both current sum and its 3rd power sum are zero then it is a potential palindrome, append index to list
            if cur_sum == 0 and cur_sum_cubued == 0:
                zero_pos.append(i)

        # check from last index if it is indeed a palindrome and not
        # just repeating last character which can also result in zero for both sums
        max_palindrome_pos = 0
        for pos in zero_pos[::-1]:
            sub = s[:pos+1]
            if sub == sub[::-1]:
                max_palindrome_pos = pos
                break

        prefix = s[max_palindrome_pos+1:]
        return prefix[::-1]+s
