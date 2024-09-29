class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # print(f'{nums}, {target}')
        
        def binarySearch(start, end, target):
            print(f'on {start} {end} {target}')
            if target<=nums[start]:
                # print(f'match start at index {start} of number {nums[start]}, type {type(start)}')
                return start
            elif nums[end]==target:
                # print(f'match end at index {end} of number {nums[end]}, type {type(end)}')
                return end
            elif target>nums[end]:
                return end+1

            mid = start+int((end-start)/2) # don't forget to add start to get right index of subsequent recursion iterations

            # print(f'indexs {start},{mid},{end}')
            if target <= nums[mid]:
                # print(f'target {target} smaller than mid {nums[mid]} at index {mid}, searching from {start} to {mid}')
                return binarySearch(start, mid, target)
            else:
                # print(f'target {target} greater or equal than mid {nums[mid]} at index {mid}, searching from {mid+1} to {end}')
                return binarySearch(mid+1, end, target)

        r = binarySearch(0,len(nums)-1,target)
        # print(f'r is of type {type(r)}')
        return r
