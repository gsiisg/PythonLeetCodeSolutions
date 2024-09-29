class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # works for only words that do not combine to form elements in s
        # e.g. s="cars" wordDict=["car","ca","rs"]
        # for word in wordDict:
        #     s = s.replace(word,'')

        # return s==''


        # Takes too long without memoization
        # lenDict = defaultdict(list)
        # for word in wordDict:
        #     lenDict[len(word)].append(word)

        # self.result = []
        # self.alreadyChecked=[]

        # def checkExist(s):
        #     print(f'checking s {s}')
        #     if s=='':
        #         self.result.append(1)
        #         print(f'confirmed since s is empty')
        #         return

        #     print(f'already checked is {self.alreadyChecked}')
        #     if not(s in self.alreadyChecked):
        #         for wordlen in lenDict.keys():
        #             print(f'check if wordlen {wordlen} "{s[:wordlen]}" in wordDict')
        #             prefix = s[:wordlen]
        #             if prefix in wordDict:
        #                 print(f'left over try "{s[wordlen:]}"')
        #                 sLeft = s[wordlen:]
        #                 self.alreadyChecked.append(s[:wordlen])
        #                 checkExist(sLeft)
        #             else:
        #                 print(f'prefix {prefix} not in wordDict')

        # checkExist(s)

        # return sum(self.result) > 0

        lenDict = defaultdict(list)
        for word in wordDict:
            lenDict[len(word)].append(word)

        mem = {}

        def exist(s):
            if not s:
                # if nothing left, that means original s is confirmed True
                return True
            
            # return mem of s for early stop
            if s in mem:
                return mem[s]

            for wordlen in lenDict.keys():
                prefix = s[:wordlen]
                suffix = s[wordlen:]
                if prefix in lenDict[wordlen] and exist(suffix):
                    # if word is the beginning, feed the rest into recursion
                    mem[s] = True
                    return True

            # if all words checked and no match return False
            mem[s] = False

        return exist(s)            