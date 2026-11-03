class Solution:
    def isValid(self, s: str) -> bool:
        dct = {"[":"]", "(":")", "{":"}"}
        stack = [el for el in s]
        for sk in stack:
            if sk in dct:
                pass

        return True


s = Solution()
print(s.isValid("()"))
