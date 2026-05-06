class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float("inf")
        maxProfit = 0

        for price in prices:

            if price < minSoFar:
                minSoFar = price
            else:
                currProfit = price - minSoFar
                maxProfit = max(maxProfit, currProfit)
        
        return maxProfit