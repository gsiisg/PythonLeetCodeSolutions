class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):
            return -1

        tot_gas = 0
        around = 0
        smallest_gas = 0

        # when smallest gas encountered, should start afterward to avoid running out of gas
        for i in range(len(gas)):
            tot_gas += gas[i]-cost[i]
            if tot_gas < smallest_gas:
                around = i+1
                smallest_gas = tot_gas

        return around