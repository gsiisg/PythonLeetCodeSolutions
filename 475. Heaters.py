class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # brute force
        radius_needed = 0

        heater = 0

        houses = sorted(set(houses)) # there's a dupe in dataset needed to be sorted(set()) in a test case
        heaters = sorted(set(heaters))

        # assume more houses than heaters
        for house in houses:

            # while there's next heater, and next heater is closer, go to next heater
            while heater + 1 < len(heaters) and (abs(house-heaters[heater+1]) <= abs(house-heaters[heater])):

                heater += 1

            radius_needed = max(radius_needed, abs(house-heaters[heater]))

        return radius_needed


            