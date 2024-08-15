class Solution:
    def hIndex(self, citations: List[int]) -> int:


        a = sorted(citations)[::-1]
        for i in range(len(a)):
            if i>=a[i]:
                return i

        if a[i] > i:
            return len(a)

        return 0