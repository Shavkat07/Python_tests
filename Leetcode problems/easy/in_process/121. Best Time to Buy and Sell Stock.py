from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		min_price = prices[0]
		profit = 0
		for i in prices:
			if profit < i - min_price:
				profit = i - min_price
			if min_price > i:
				min_price = i
		return profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
