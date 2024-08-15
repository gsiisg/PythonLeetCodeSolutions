#!/usr/bin/env python
"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

# following the thread on leetcode:
# https://discuss.leetcode.com/topic/39526/python-solution/4
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []
        result = []
        worddict = {word[::-1]: i for i, word in enumerate(words)} # reverse the words because we are looking for its compliment in pre/post-fix
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, postfix = word[:j], word[j:] # split word into pre/post-fix
                # if conditions are satisfied, that means the postfix can be swapped and the prefix cannot
                # so find the prefix (compliment) in worddict and if it is there it can form a palindrome
                # e.g. pre:"ab"  post:"cdc" need to find "ba" in dict, but look for "ab" the same pre, since dict has the reverse
                if prefix in worddict and i != worddict[prefix] and postfix==postfix[::-1]:
                    result.append((i, worddict[prefix]))
                # likewise reversing pre/post-fix, but needs j > 0 or prefix will be empty
                if j > 0 and postfix in worddict and i != worddict[postfix] and prefix==prefix[::-1]:
                    result.append((worddict[postfix], i))
        return result
