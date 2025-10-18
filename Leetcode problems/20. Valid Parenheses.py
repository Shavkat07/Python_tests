class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counter = 0
        for ch in s:
            counter += 1
            stack.append(ch)
            if counter % 2 == 0:
                if stack[-2] != stack[-1::-1]:
                    return False


        return True


s = Solution()
print(s.isValid("()"))
