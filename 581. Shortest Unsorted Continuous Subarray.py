class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1

        while (l < r):
            if (nums[l] <= nums[l + 1]) and (nums[r] >= nums[r - 1]):
                l += 1
                r -= 1
            elif nums[l] <= nums[l + 1]:
                l += 1
            elif nums[r] >= nums[r - 1]:
                r -= 1
            else:
                break

        if l == r:
            return 0

        # search within the unsorted range if any number is smaller or bigger than outside
        # if so extend the range to left or right
        for i in range(l, r + 1):
            while (l - 1 >= 0) and (nums[i] < nums[l-1]):
                l -= 1
            
            while (r + 1 < len(nums)) and (nums[i] > nums[r+1]):
                r += 1

        return r - l + 1

        # # brute force 50-70%
        # sorted_nums = sorted(nums)

        # min_index, max_index = None, None

        # length = len(nums)

        # for i in range(length):
        #     if sorted_nums[i] != nums[i]:
        #         min_index = i
        #         break

        # if min_index is None:
        #     return 0

        # for i in range(length):
        #     reverse_index = len(nums)-1-i
        #     if sorted_nums[reverse_index] != nums[reverse_index]:
        #         max_index = reverse_index
        #         break

        # return max_index - min_index + 1
            