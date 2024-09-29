class Solution:
    def partition(self, s: str) -> List[List[str]]:

        all_sub_pal = defaultdict(list)

        # initialize prefix dict
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                if sub==sub[::-1]:
                    all_sub_pal[len(sub)].append(sub)
        
        partitions = []

        print(f'all_sub_pal {all_sub_pal}')

        def check(prefix, suffix):

            # once a prefix consist of the entire string s, add to partitions
            if suffix == '':
                # print(f'adding prefix {prefix}')
                partitions.append(prefix)
                # print(f'partitions now {partitions}')

            for i in range(1,len(suffix)+1):
                sub = suffix[:i]
                temp_prefix = prefix+[sub]
                temp_suffix = suffix[i:]
                # print('temp',temp_prefix, temp_suffix)
                if sub in all_sub_pal[len(sub)]:
                    check(temp_prefix, temp_suffix)

        check([], s)

        return partitions
