class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result_index = 0
        check_index = 0
        length = len(nums)
        while check_index < length:
            # print(f'set result_index {result_index} to check_index {check_index}')
            nums[result_index] = nums[check_index]
            result_index += 1
            check_index += 1

            # give it the chance to repeat once, increment index
            # originally thought problem was no repeat, but found max 1 repeat, so added this section
            if check_index < length and (nums[result_index-1] == nums[check_index]):
                nums[result_index] = nums[check_index]
                result_index += 1
                check_index += 1

            # print(f'result_index {result_index}, check_index {check_index}')
            while (check_index < length) and (nums[check_index] == nums[check_index - 1]):
                check_index += 1
                # print(f'check_index {check_index}')

        return result_index