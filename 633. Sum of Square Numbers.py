class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # iterate till sqrt of the number
        squared_list = []

        for i in range(int(math.sqrt(c))+1):
            squared_list.append(i*i)

        # print(squared_list)

        l, r = 0, len(squared_list)-1

        # head tail search pattern
        while l <= r:
            num_l, num_r = squared_list[l], squared_list[r]
            if num_l + num_r  == c:
                return True

            elif num_l + num_r < c:
                l += 1

            else:
                r -= 1

        return False
