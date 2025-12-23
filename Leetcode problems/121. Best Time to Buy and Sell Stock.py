from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profits = []
		cntr = 0
		cntr2 = 1
		while cntr != len(prices)-1:
			if prices[cntr] < prices[cntr2]:
				profits.append(prices[cntr2] - prices[cntr])
			cntr2 += 1
			if cntr2 == len(prices):
				cntr += 1
				cntr2 = cntr + 1
				
		return max(profits) if profits else 0


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
