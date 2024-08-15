class Solution:
    def jump(self, nums: List[int]) -> bool:

        # keep track of furthest it can reach at each iteration
        steps = 0
        furthest_attempt = 0
        furthest_so_far = 0
        end_index = len(nums) - 1

        for i in range(end_index):
            furthest_so_far = max(furthest_so_far, i + nums[i])
            if furthest_so_far >= end_index:
                steps += 1
                break

            # gone through all previous steps and couldn't get past the furthest attempt
            # then increment steps
            if i == furthest_attempt:
                steps += 1
                furthest_attempt = furthest_so_far

        return steps

        return ans
            



        # still takes too long
        # self.min_steps = float('inf')

        # length = len(nums)
        # if length < 2:
        #     return 0

        # end_nums_index = length - 1

        # # guarantee to reach end, backward was running out of time, try forward search
        # def longestJump(end_index, steps):
        #     # find possible starts from the back
        #     possible_start = []
        #     for start_index in range(0, end_index):
        #         if start_index + nums[start_index] >= end_index:
        #             if start_index == 0:
        #                 # terminate if goal reached
        #                 # print('found min steps')
        #                 self.min_steps = min(self.min_steps,steps+1)
        #                 return self.min_steps
        #             else:
        #                 longestJump(start_index, steps+1)
                    
                
        #     return self.min_steps
            
        # return longestJump(end_nums_index, 0)

        # return self.min_steps


            











        # TOOK TOO LONG
        # # reverse the list first
        # length = len(nums)
        # start_index = length-2 # start from back
        # end_index = length-1

        # if length < 2:
        #     return 0

        # self.steps = float(inf)

        # def canReach(start_index, end_index, step):
        #     # print(start_index,end_index,step, self.steps)
        #     if (step > self.steps) or (start_index == -1):
        #         return
                
        #     if (nums[start_index] >= end_index - start_index):
        #         if start_index == 0:
        #             # this is success
        #             # print('last jump from',start_index,end_index,step)
        #             self.steps = min(self.steps,step+1)

        #         # partial success, continues to search in remaining section 
        #         # using the old start_index as end_index but add one step
        #         # print('partial jump from',start_index,end_index,step)

        #         canReach(start_index-1, start_index, step+1)

        #     # keep searching extending start toward front
        #     canReach(start_index-1, end_index, step)

        # canReach(start_index, end_index, 0)

        # # print(self.steps)

        # return self.steps