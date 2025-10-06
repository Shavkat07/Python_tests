class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_clone = 0
        for i in t:
            if s_clone < len(s) and s[s_clone] == i:
                s_clone += 1

        return s_clone == len(s)

s = Solution()
print(s.isSubsequence(s = "ab", t = "baab"))

