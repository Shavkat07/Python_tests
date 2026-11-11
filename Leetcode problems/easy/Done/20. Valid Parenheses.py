class Solution:
	def isValid(self, s: str) -> bool:
		dct = {"[": "]", "(": ")", "{": "}"}
		stack = []
		if len(s) <= 1:
			return False
		for sk in s:
			if dct.get(sk):
				stack.append(sk)
			elif len(stack)!=0 and dct.get(stack[-1]) == sk:
				stack.pop()
			else:
				return False
		if len(stack) != 0: return False
		return True


s = Solution()
print(s.isValid("("))
