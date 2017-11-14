#!/usr/bin/env python
"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.



https://discuss.leetcode.com/topic/47336/easy-to-understand-python-solution-can-generalized-to-0-to-9/2

A cycle is 0~9 for one position. 1 appears a certain number of times in each cycle.

For example, given number 32107.

At position 7, 1 appears 3210 complete cycles, and within each cycle 1 appears once. Also, because 7 > 1,
    so it can be regarded as one more complete cycle. In total 1 appears 3211 times at position 7.

At position 0, 1 appears 321 complete cycles, and within each cycle 1 appears 10 times, eg, ...10-...19.
    In total 1 appears 321 * 10 times at position 0.

At position 1, 32 complete cycles, and within each cycle 1 appears 100 times, eg, ..100-..199.
    Notice here it is 1, so it has incomplete cycle from 32100-32107, which is 32107 % 100 + 1 = 8 times.
    In total 1 appears 32 * 100 + 8 times at position 1.

So on so forth.

A generalized code for any digit 0 ~ 9 is below.
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count_digit(n, digit):
            # counter for number of times a certain digit appears
            count = 0

            # place of digit that is being counted, start as 1 then 10 then 100 etc
            digitPlace = 1

            while digitPlace <= n:

                # initialize the number of cycles, and the remainder from n
                cycles, remainder = divmod(n, digitPlace)
                # current digit is the last digit of cycles, so take cycles // 10.
                # E.g. for 321 current digit is 1 by taking 321 // 10 = 32
                currentDigit = cycles % 10


                if currentDigit > digit:
                    # the number of times the currentDigit will appear as 'digit' if currentDigit > digit is:
                    # number of complete cycles (cycles//10) plus the extra one (+1) since the last digit current digit
                    # surpasses digit.  Then everything has to be multiplied by the digitPlace
                    # So total count for this digit is (cycles // 10 + 1) * digitPlace
                    # e.g. 32107 counting the 1,000th place and counting digit of '1'
                    # 1 appeared 30//10 = 3 full cycles for 01, 11, 21, 31 for the 1,000th place so multiply by
                    # digitPlace 1000
                    count += (cycles // 10 + 1) * digitPlace

                elif currentDigit == digit:
                    # if the currentDigit IS the digit being counted, then the number of occurrence
                    # are the full cycles + remainder + 1
                    # e.g. 32107 counting the 100th place
                    # 1 appeared 321//10=32 * 100 times + the remainder+1 = 100, 101, 102... 107 = 7+1 times
                    count += (cycles // 10) * digitPlace + remainder + 1

                else:
                    # no remainder+1 just count full cycles
                    count += (cycles // 10) * digitPlace

                # increment digitPlace by 10 for next digit
                digitPlace *= 10
            return count
        return count_digit(n, 1)





