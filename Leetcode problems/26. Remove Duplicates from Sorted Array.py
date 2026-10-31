class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                del nums[l]
                continue
            l += 1
            r += 1
        return r, nums
s = Solution()
print(s.removeDuplicates([0,0,0,1,1,1,2,2,3,3,4]))