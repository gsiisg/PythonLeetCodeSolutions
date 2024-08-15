class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rnums=nums[::-1]

        # start with [1], skip last element
        forward_prod = 1
        forward = [1]
        
        backward_prod = 1
        backward = [1]

        for i in range(len(nums)-1):
            forward_prod *= nums[i]
            forward.append(forward_prod)
            backward_prod *= rnums[i]
            backward.append(backward_prod)

        backward = backward[::-1]

        p = []
        for i in range(len(nums)):
            p.append(forward[i]*backward[i])

        return p
