class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # reverse the list first
        start_index = len(nums)-1 # start from back
        end_index = len(nums)-1

        def canReach(start_index, end_index):

            if (nums[start_index] >= end_index - start_index):
                if start_index == 0:
                    return True
                else:
                    # partial success, continues to search in remaining section using the old start_index as end_index
                    return canReach(start_index-1, start_index)
            else:
                # this extend the remaining section toward the front while maintaining the end_index
                if start_index == 0:
                    return False
                return canReach(start_index-1, end_index)

        return canReach(start_index, end_index)
    
    # FIRST TRY SUCCESS!

