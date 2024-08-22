class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        # notice the X doesn't matter, relative positions of L, R stays the same before and after
        # e.g L and R cannot cross
        # L can only move left, smaller/equal ending index than starting
        # R can only mnove right, greater/equal ending index than starting
        reduced_start = []
        reduced_start_index = []
        for i, letter in enumerate(start):
            if letter!='X':
                reduced_start.append(letter)
                reduced_start_index.append(i)

        reduced_end = []
        reduced_end_index = []
        for i, letter in enumerate(end):
            if letter!='X':
                reduced_end.append(letter)
                reduced_end_index.append(i)

        if reduced_start != reduced_end:
            return False

        for i in range(len(reduced_start_index)):
            letter = reduced_start[i]

            if (letter == 'L') and (reduced_start_index[i] < reduced_end_index[i]):
                return False
            if (letter == 'R') and (reduced_start_index[i] > reduced_end_index[i]):
                return False

        return True


        # Tried to reproduce steps to convert start to end, more complicated than thought, failed
        # start = list(start)
        # end = list(end)

        # def swap(letter, letter_list, end):
        #     for i in range(1,len(start)):
            
        #         if letter_list[i]==letter and letter_list[i-1] == 'X' and ((letter_list[i] != end[i]) or (letter_list[i-1] != end[i-1])):
        #             switch_index = i

        #             while (letter_list[switch_index]==letter and letter_list[switch_index-1] == 'X') and \
        #             ((letter_list[switch_index] != end[switch_index]) or (letter_list[switch_index-1] != end[switch_index-1])):
        #                 # print('swapping', index-1, index, letter_list)
        #                 print(f'before swaps', letter_list)

        #                 letter_list[switch_index-1], letter_list[switch_index] = \
        #                 letter_list[switch_index], letter_list[switch_index-1]
        #                 print(f'after swaps', letter_list)

        #                 switch_index -= 1

        #     return letter_list

        # letter_list = swap('L', start, end)

        # print('doing the reverse', letter_list[::-1], end[::-1])
        # letter_list = swap('R', letter_list[::-1], end[::-1])

        # letter_list = letter_list[::-1]
        # print(letter_list)

        # # print(start,end)
        # return letter_list==end