class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        if length==1 or k==0:
            return

        if length==k:
            return

        k = k % length

        # Always taking the popped then place it at new location will not work if k divides into length perfectly
        # have to loop over all elements
        index = k
        source_num = nums[0]
        destination_num = nums[index]

        # times = length/k
        # divisible = not (times*10) % 10
        # print(divisible, times)
        count=1

        touched_index=set()

        for i in range(length):
            # print(f'iteration {i}')

            # if divisible and (i>1) and (i%times == 0) and k!=1:
            if index in touched_index: # USE THIS TO KEEP TRACK WHEN TO SHIFT
                # print('### perfectly divisible, switch to next index')
                index = (k+count) % length
                # print(f'new index {count}')
                source_num = nums[count]
                # print(f'new source_num {source_num}')
                destination_num = nums[count+k]
                # print(f'new destination_num {destination_num}')
                count += 1
            
            # place source_num to index
            touched_index.add(index)
            nums[index] = source_num
            # print(f'placing {source_num} at index {index}')
            source_num = destination_num 
            # print(f'source_num is now {destination_num}')
            index = (index + k) % length
            # print(f'new index is {index}')
            destination_num = nums[index]
            # print(f'destination_num is now {nums[index]} from index {index}')


