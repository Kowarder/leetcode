class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        mx = 0
        while i < j:
            mx = max(min(height[i], height[j])*(j-i), mx)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx
