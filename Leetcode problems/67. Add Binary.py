class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        return str(bin(a + b))[2::]



s = Solution()
print(s.addBinary('1010', '1011'))
