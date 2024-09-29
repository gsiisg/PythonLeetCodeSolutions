class Solution:
    def rob(self, nums: List[int]) -> int:

        # works but very slow ~35%        
        # if not nums:
        #     return 0

        # length = len(nums)
        # print(f'length {length}')

        # if length==1:
        #     return nums[0]
        # elif length==2:
        #     return max(nums)
        # elif length==3:
        #     # modified from rob
        #     return max(nums[1],nums[2]-nums[0],nums[0],nums[2])

        # # reuse code from 198. House Robber
        # def modrob(nums):

        #     print(nums)
        #     if not nums:
        #         return 0

        #     length = len(nums)
        #     print(f'length {length}')

        #     if length==1:
        #         return nums[0]
        #     elif length==2:
        #         return max(nums)
        #     elif length==3:
        #         nums[2] = nums[0]+nums[2]
        #         return max(nums[1],nums[2])

        #     # for each element after the 2nd
        #     # the value set to the total if that step is used
        #     # don't worry about the step of an element skipped, just don't record on it
        #     # at the end pick the max of last two, because the 2nd to last will have last element skipped
        #     nums[2] = nums[0]+nums[2]

        #     for i in range(3, length):
        #         nums[i] = nums[i]+max(nums[i-2], nums[i-3])

        #     return nums[-1]

        # # print(nums)
        # # several scenarios
        # # with gap size of 1
        # # ...-2...0...
        # # ...-1...1...
        # # with gap size of 2
        # # ...-3...0...
        # # ...-2...1...
        # # ...-1...2...
        # possible = []
        # possible.append(modrob(nums[:-1]))
        # possible.append(modrob(nums[1:]))
        # possible.append(modrob(nums[:-2]))
        # possible.append(modrob(nums[1:-1]))
        # possible.append(modrob(nums[2:]))
        
        # return max(possible)
        length = len(nums)
        if length==1:
            return nums[0]
        elif length==2:
            return max(nums)
        elif length==3:
            # nums[2] = nums[0]+nums[2]
            # mod from old rob
            return max(nums[0],nums[1],nums[2])
            
        def modrob(nums):
            length = len(nums)
            if length==1:
                return nums[0]
            elif length==2:
                return max(nums)
            elif length==3:
                nums[2] = nums[0]+nums[2]
                return max(nums[1],nums[2])

            # for each element after the 2nd
            # the value set to the total if that step is used
            # don't worry about the step of an element skipped, just don't record on it
            # at the end pick the max of last two, because the 2nd to last will have last element skipped
            nums[2] = nums[0]+nums[2]

            for i in range(3, length):
                nums[i] = nums[i]+max(nums[i-2], nums[i-3])

            return max(nums[-1],nums[-2])

        return max(modrob(nums[:-1]),modrob(nums[1:]))