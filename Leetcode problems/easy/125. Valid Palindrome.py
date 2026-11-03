class Solution:
	def isPalindrome(self, s: str) -> bool:
		a = [i.lower() for i in s if i.isalnum()]
		return a == a[::-1]
		
s = Solution()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))