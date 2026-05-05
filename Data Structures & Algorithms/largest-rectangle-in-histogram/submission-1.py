class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # sentinel to avoid clean up pass at the end for bars that never get popped
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                prevIdx = stack.pop()
                prevHeight = heights[prevIdx]

                leftBdry = stack[-1] if stack else -1
                width = i - leftBdry - 1

                area = width * prevHeight
                maxArea = max(maxArea, area)
            
            stack.append(i)
        
        return maxArea
