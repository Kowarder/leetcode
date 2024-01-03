class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        water = 0
        i, j = 0, len(height)-1
        lm, rm = height[0], height[-1]
        while i <= j:
            if height[i] > lm:
                lm = height[i]
            if height[j] > rm:
                rm = height[j]
            
            if lm <= rm:
                water += lm - height[i]
                i += 1
            else:
                water += rm - height[j]
                j -= 1
        return water
