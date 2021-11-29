class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        diff = 0
        left = 0
        right = N - 1
        while left < right:
            if nums[left] == 0:
                nums.remove(0)
                diff += 1
                right -= 1
            else:
                left += 1
        nums.extend([0]*diff)
        print(nums)
        
            