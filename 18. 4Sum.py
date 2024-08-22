from collections import defaultdict
from math import ceil

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # previous method took too long
        # try using two pointers on the keys after sorting keys

        if len(nums) < 4:
            return []

        length = len(nums)
        add_dict = defaultdict(list)

        for i in range(length):
            for j in range(i+1, length):
                # print(i,j)
                add_dict[nums[i]+nums[j]].append([i,j])

        # print(add_dict)
        keys = sorted(add_dict.keys())

        all_quadruplets = []
        already_added_tuples = set()

        # assign lists
        l, r = 0, len(keys)-1
        list1 = add_dict[keys[l]]
        list2 = add_dict[keys[r]]


        # print(list1,list2)

        while l <= r:
            list1 = add_dict[keys[l]]
            list2 = add_dict[keys[r]]
            if keys[l] + keys[r] == target:
                # print(f'found key {keys[l]}:{list1} {keys[r]}:{list2}')
                for i in range(len(list1)):

                    curr_tuple = nums[list1[i][0]],nums[list1[i][1]] 
                    prev_tuple = nums[list1[i-1][0]],nums[list1[i-1][1]]
                    
                    # early stopping need it to get past 288/294
                    if i>0 and (curr_tuple == prev_tuple):
                        # print(f'skipping {curr_tuple}, identical to prev_tuple {prev_tuple}')
                        continue
                    for j in range(len(list2)):
                        # check if there are repeated indices
                        total_list = list1[i] + list2[j]
                        # print(f'total list {total_list}')
                        quadruplets = []
                        for k in range(4):
                            quadruplets.append(nums[total_list[k]])
                        sorted_quadruplets_tuple = tuple(sorted(quadruplets))

                        if sorted_quadruplets_tuple not in already_added_tuples and len(set(total_list))==4:
                            already_added_tuples.add(sorted_quadruplets_tuple)
                            all_quadruplets.append(quadruplets)
                            print(f'adding {quadruplets}')

                l += 1
                r -= 1


            elif (keys[l] + keys[r] < target):
                l += 1

            else:
                r -= 1

        return all_quadruplets










        # 287/294 cases, Time Limit Exceeded
        # # for every pair use their total as key and the two indices as values
        # length = len(nums)
        # add_dict = defaultdict(list)

        # for i in range(length):
        #     for j in range(i+1, length):
        #         add_dict[nums[i]+nums[j]].append([i,j])

        # keys = list(add_dict.keys())
        # # print(keys)

        # all_quadruplets = []
        # already_added_tuples = set()
        # # print(add_dict)

        # # half_keys = ceil(len(keys)/2)

        # for i in range(len(keys)):
        #     key = keys[i]
        #     complement_key = target-key
        #     # print('keys',key, complement_key)

        #     if (complement_key in keys):
        #         # print('keys',key, complement_key)
        #         list1 = add_dict[key]
        #         list2 = add_dict[complement_key]
        #         for j in range(len(list1)):
        #             for k in range(len(list2)):
        #                 # check if there are repeated indices
        #                 total_list = list1[j] + list2[k]
        #                 if len(set(total_list))==4:
        #                     # print('total_list',total_list)
        #                     quadruplets = []
        #                     for l in range(4):
        #                         quadruplets.append(nums[total_list[l]])
        #                     sorted_quadruplets = tuple(sorted(quadruplets))
        #                     if sorted_quadruplets not in already_added_tuples:
        #                         already_added_tuples.add(sorted_quadruplets)
        #                         all_quadruplets.append(quadruplets)

        # return all_quadruplets



        