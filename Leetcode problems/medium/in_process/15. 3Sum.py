import time
starttime = time.time()

class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		# x, y, z = 0, 1, 2
		nums = sorted(nums)
		res = []
		for i in range(len(nums)):
			target = nums[i]
			new = nums[i + 1:]
			diff = {-target-new[k]:k for k in range(len(new))}
			
			for j in range(i+1, len(nums)):
				if nums[j] in diff:
					res.append([target, nums[j], new[diff[nums[j]]]])
			
		
		return res


nums = [-4, -1, -1, 0, 1, 2]
nums2 = [-4, 0, 4]
nums3 = [-4, -2, 0, 6]
nums4 = [-4, -2, -1, -1, 1, 3, 4, 6]
diff = {-2:0, -3:1, -3:1, }
# nums5 = [0,0,0]
s = Solution()
print(s.threeSum(nums4))
end = time.time()
print(end-starttime)
