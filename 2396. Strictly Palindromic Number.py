class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def numToBase(n, base):
            digits = []
            while n:
                n, m = divmod(n, base)
                digits.append(m)
            return digits[::-1]

        def isPalindrome(num_list):
            # return num_list == num_list[::-1]
            length = len(num_list)
            l, r = 0, length-1
            while l < r:
                if num_list[l] != num_list[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        for i in range(2,n-1):
            num_list = numToBase(n, i)
            # print(num_list)
            if not isPalindrome(num_list):
                # print(num_list, 'is not palindrome')
                return False
        
        return True