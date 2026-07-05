class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left_max = 0
        right_max = 0

        total_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            curr_level = 0
            if height[left] < height[right]:
                curr_level = left_max - height[left]
                left_max = max(height[left], left_max)
                left += 1

            else:
                curr_level = right_max - height[right]
                right_max = max(height[right], right_max)
                right -= 1
            
            if curr_level > 0: total_water += curr_level



        return total_water