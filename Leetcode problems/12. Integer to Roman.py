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

class Solution:
    def intToRoman(self, num: int ) -> str:
        int_to_roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V',1: 'I'}
        answer = ''
        lst = []
        lst2 = []
        counter = 1
        for i in str(num)[::-1]:
            lst.append(int(i) * counter)
            counter *= 10

        for i in lst[::-1]:

            if i in int_to_roman:
                lst2.append(i)
                counter //= 10
            else:
                # if i + counter ==
                pass
        print(lst)
        return answer

sol = Solution()
sol.intToRoman(1994)

# 'MCMXCIV'

# 1994 ---> [1000,100,1000,10,100,1,5]
# 199 ---> [100, 10, 100, 1, 10] CXCIX
#MCC
# 90 = 10, 100
# 80 = 50, 10, 10, 10
# 60 = 50, 10
# 40 = 10, 50
# 30 = 10, 10, 10
# 20 = 10, 10
# 10 = 10
