#!/usr/bin/env python
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

https://discuss.leetcode.com/topic/8714/clear-python-code
"""

class Solution(object):
    def divide(self, numerator, denominator):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # sets the sign of the result, 1 if positive, 0 if negative
        sign = (numerator > 0) == (denominator > 0)
        # use the absolute values for calculations, sign already taken care of
        numerator, denominator = abs(numerator), abs(denominator)
        result = 0
        while numerator >= denominator:
            # want to divide numerator by a temporary denominator that will increase by x2 each time
            # to speed up the calculation
            tempDenominator = denominator
            # factor will keep track of how many x2 there have been to the temporary denominator
            factor = 1
            while numerator >= tempDenominator:
                # for each subtraction of temporary denominator, add the factor to result
                # The remaining numerator will always be positive because the while condition
                # ensures that numerator is always greater or equal to temporary denominator
                # when temporary denominator gets too big, it goes to the first while loop
                # and reset factor to 1 and reset temporary denominator to denominator the original value
                numerator -= tempDenominator
                result += factor
                factor <<= 1
                tempDenominator <<= 1
        # if result has a negative sign, then report the 0-result
        if not sign:
            result = -result

        return min(max(-2147483648, result), 2147483647)
