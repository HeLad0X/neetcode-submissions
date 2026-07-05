class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        curr_max = 0
        for i, n in enumerate(height):
            left_max[i] = curr_max
            curr_max = max(curr_max, n)

        curr_max = 0
        for i in range(len(height) - 1, 0, -1):
            right_max[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        total_water = 0
        for i, n in enumerate(height):
            water_level = min(left_max[i], right_max[i]) - height[i]
            if water_level > 0: total_water += water_level

        return total_water