"""Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV


Constraints:

1 <= num <= 3999
"""
import time


class Solution:
	def intToRoman(self, num):
		values = {
			1: "I",4: "IV",	5: "V",	9: "IX", 10: "X",40: "XL",50: "L",90: "XC",100: "C",400: "CD",500: "D",900: "CM",1000: "M"
		}
		result = ""
		
		for key in sorted(values.keys(), reverse=True):
			while num >= key:
				result += values[key]
				num -= key
		
		return result

start = time.time()
sol = Solution()
print(sol.intToRoman(1993), 'time was: ', time.time() - start)

# 1994 --->[1000 + 900 + 90 + 4] --> [1000,100,1000,10,100,1,5] MCMXCIV
# 199 ---> [100, 10, 100, 1, 10] CXCIX
# MCC
# 90 = 10, 100
# 80 = 50, 10, 10, 10
# 60 = 50, 10
# 40 = 10, 50
# 30 = 10, 10, 10
# 20 = 10, 10
# 10 = 10


# 1 = 1
# 2 = 1, 1
# 3 = 1, 1, 1
# 4 = 1, 5
# 5 = 5
# 6 = 5, 1
# 7 = 5, 1, 1
# 8 = 5, 1, 1, 1
# 9 = 1, 10
# 10 = 10
