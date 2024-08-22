class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        length = len(arr)
        l, r = 0, length - 1

        # print(l, r)
        while (l + 1 < length) and (arr[l] <= arr[l+1]):
            l += 1

        # early stop here if conditions statisfied
        if l == length-1:
            return 0

        while (r - 1 >= 0) and arr[r] >= arr[r-1]:
            r -= 1

        min_remove = length - 1
        # print(l, r, min_remove)

        # set original goal post to be l, r
        # retreat when nothing satisfies the requirements, l toward left, r toward r
        for left in range(l,-1,-1):
            for right in range(r, length):
                # print(f'checking {left}, {right}')
                remove = right - left - 1
                if remove >= min_remove:
                    # print(f'{left}, {right} not smaller than min_remove', min_remove)
                    break # early stop with break, don't use continue, continue will calc useless trials
                if arr[left] <= arr[right]:
                    min_remove = remove
                    # print(f'new remove from {left} to {right} of {min_remove}')
                elif right == length-1:
                    min_remove = right - left
                elif left == 0:
                    min_remove = right - left

        # min_remove = min(length-1, min_remove)
        
        return min_remove