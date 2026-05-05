class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i in range(n):
            currHeight = heights[i]

            while stack and currHeight < heights[stack[-1]]:
                prevIdx = stack.pop()
                prevHeight = heights[prevIdx]

                leftBdry = stack[-1] if stack else -1
                width = i - leftBdry - 1

                area = width * prevHeight
                maxArea = max(maxArea, area)
            
            stack.append(i)
        
        # handling bars that never got popped
        while stack:
            prevIdx = stack.pop()
            prevHeight = heights[prevIdx]

            leftBoundary = stack[-1] if stack else -1
            width = n - leftBoundary - 1

            maxArea = max(maxArea, prevHeight * width)
        
        return maxArea
