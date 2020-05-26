# 953. Verifying an Alien Dictionary
#
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
#
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = [x for x in range(len(order))]
        alien_dict = dict(zip(order, index))

        def alien_lookup(word):
            # create a list of numbers indicating order of letter from word
            order_list = []
            for letter in word:
                order_list.append(alien_dict[letter])
            return order_list

        first_word = alien_lookup(words[0])

        for i in range(len(words) - 1):
            # if new word is greater, move to next pair of words, else return false
            # can speed up with early stopping when each new letter of the new word is known
            # phase 2 if words are long implement early stopping
            second_word = alien_lookup(words[i + 1])
            if first_word < second_word:
                first_word = second_word
            else:
                return False
        # if no false after all words checked, then return True
        return True