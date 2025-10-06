# class Solution:
# 	def lengthOfLongestSubstring(self, s: str) -> int:
# 		if s is None or len(s) == 0:
# 			return 0
# 		if s.isspace() or len(s) == 1:
# 			return 1
# 		pointer1 = 0
# 		pointer2 = 1
# 		substring = []
# 		substrings = []
# 		substring.append(s[pointer1])
# 		while True:
# 			if s[pointer2] in substring:
# 				pointer1 += 1
# 				pointer2 = pointer1 + 1
# 				substrings.append(''.join(substring))
# 				substring = [s[pointer1]]
# 			else:
# 				substring.append(s[pointer2])
# 				pointer2 += 1
# 				print(substring)
#
# 			if pointer2 >= len(s) - 1:
# 				substrings.append(''.join(substring))
#
# 			if pointer1 >= len(s) - 1 or pointer2 >= len(s) - 1:
# 				lens = [len(i) for i in substrings]
# 				print(substrings)
# 				return max(lens)
#
#
# cls = Solution()
# print(cls.lengthOfLongestSubstring("aab"))


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if s is None or len(s) == 0:
			return 0
		if s.isspace() or len(s) == 1:
			return 1
		
		k = 0
		substring = ''
		arr_substrings = []
		while True:
			if s[k] in substring:
				k += 1
				arr_substrings.append(substring)
				substring = ''
				
			else:
				substring += s[k]
				k+=1
			
			
			
			print('bu substring', substring)
			print('bu array' ,arr_substrings)
			
		

cls = Solution()
print(cls.lengthOfLongestSubstring("abcabcbb"))




