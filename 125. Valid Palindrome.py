class Solution:
    def isPalindrome(self, s: str) -> bool:

        length = len(s)

        if length < 2:
            return True

        lower_case = 'abcdefghijklmnopqrstuvwxyz0123456789'
        l, r = 0, length-1
        while l < r:
            left_letter = s[l].lower()
            while (left_letter not in lower_case) and (l < r):
                l += 1
                left_letter = s[l].lower()
            right_letter = s[r].lower()
            while (right_letter not in lower_case) and (l < r):
                r -= 1
                right_letter = s[r].lower()

            l += 1
            r -= 1

            if left_letter != right_letter:
                # print(left_letter, right_letter)
                return False

        return True

        
