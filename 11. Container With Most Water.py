class Solution:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)

        if length < 2:
            return 0
        
        l, r = 0, length - 1

        width = length - 1
        max_water_area = 0

        height_l, height_r = height[l], height[r]

        max_height = max(height)

        while l < r:

            max_water_area = max(max_water_area, min(height_l, height_r) * width)
            
            # early stopping (this makes rating go from ~50% to 99%)
            if max_height * (width) < max_water_area:
                break

            # doesn't matter decreasing which side when equal
            # even if one encounter a taller wall after equal, the water_area will be less
            if height_l <= height_r:
                l += 1
                height_l = height[l]
                width -= 1
            else:
                r -= 1
                height_r = height[r]
                width -= 1

        return max_water_area