#!/usr/bin/env python
'''
https://discuss.leetcode.com/topic/10484/manacher-algorithm-in-python-o-n
https://discuss.leetcode.com/topic/35399/manacher-s-algorithm-solution-in-python
'''

class Solution(object):
    def longestPalindrome(self, s):
        # pad the letters with pound
        T = '#{}#'.format('#'.join(list(s)))
        # calc length of the padded letters
        length = len(T)
        # place holder for storing the max number of palindrome elements starting from ith centers
        P = [0] * n
        # initialize center and rightEdge
        center, rightEdge = 0, 0

        for i in range(length):
            # if i is within rightEdge, then P[i] is the smaller of rightEdge-i or the mirror element P[2*center-i]
            # or else set to 1
            P[i] = min(rightEdge - i, P[2 * center - i]) if i < rightEdge else 1

            # while i+-P[i] is within (0, length), check if T elements are equal center around i
            while i - P[i] >= 0 and i + P[i] < length and T[i - P[i]] == T[i + P[i]]:
                P[i] += 1

            # if i + P[i] exceeds the rightEdge, move center to i and increase rightEdge to i+P[i]
            if i + P[i] > rightEdge:
                center, rightEdge = i, i + P[i]

        # calc maxlen and center index from P
        maxlen, c = max((m, i) for i, m in enumerate(P))
        # maxlen is the max(P)-1, -1 because need to subtract the middle element
        maxlen -= 1
        # calculate the start and end index of the palindrome
        start = c//2 - maxlen//2
        end = start + maxlen

        return maxlen, s[start:end]

s = "babcbabcbaccba"
print(Solution().longestPalindrome(s))
