class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0
        
        if sum(nums) < target:
            return 0

        # Works but too slow 18/21
        # # find first window size that sums to target
        # min_size = len(nums)
        # total = 0

        # for i in range(0,len(nums)):
        #     # print(f'i {i} current min_size is {min_size}')
        #     sub_total = 0
        #     for j in range(i,i+min_size):
        #         # print(f'sub_total {sub_total} before j {j}')
        #         if (j > len(nums)-1) or (j - i + 1 > min_size):
        #             continue
        #         sub_total += nums[j]
        #         # print(f'sub_total {sub_total} after j {j}')

        #         if sub_total >= target:
        #             min_size = j - i + 1
        #             # print(f'min_size now {min_size}')


        # Valid but only beats 5%, very
        # # try to pre compute the sum up to a point from both sides
        # total_nums = sum(nums)
        # length = len(nums)
        # forward_sum = [0]
        # total = 0
        # for i in range(length-1):
        #     total += nums[i]
        #     forward_sum.append(total)

        # backward_sum = [0]
        # total = 0
        # nums = nums[::-1]
        # for i in range(length-1):
        #     total += nums[i]
        #     backward_sum.append(total)

        # backward_sum = backward_sum[::-1]

        # # sum from i to j would be total_nums - forward_sum[i] - backward_sum[j]

        # # taking foward_sum[i] - backward_sum[j] should yield the sum(nums[i:j])

        # min_len = len(nums)
        # for i in range(len(nums)):
        #     if min_len == 1:
        #         break
        #     for j in range(min(i+min_len-1, len(nums)-1),i-1,-1):
        #         # print(min_len,i,j)
        #         check = total_nums - forward_sum[i] - backward_sum[j]
        #         if check >= target:
        #             # print(f'successfully updated min_len from {i},{j}')
        #             min_len = j - i + 1
        #         else:
        #             break


        # use two pointer to iterate to shrink window every new number added
        left = 0
        min_len = len(nums)+1 # set this to a large number e.g. length + 1 or inf
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                min_len = min(min_len, right-left+1)
                currSum -= nums[left]
                left += 1

        
        return min_len