class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            maxwater = max(maxwater, h * w)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxwater