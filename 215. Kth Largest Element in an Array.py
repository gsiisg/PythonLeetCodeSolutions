class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # Time Limit Exceedded 35/41, works but slow
        # for _ in range(k):
        #     kthmax = max(nums)
        #     nums.remove(kthmax)

        # return kthmax




        # # works but only beats ~10%
        # import heapq
        # return heapq.nlargest(k,nums)[-1]

        h = []
        for num in nums:
            heapq.heappush(h, -num)

        for i in range(k):
            ret = -heapq.heappop(h)

        return ret