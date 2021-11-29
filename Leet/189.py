class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
    
        n = len(nums)
        k %= n
        left = nums[:n-k]
        right = nums[n-k:]
        
    
    
        reverselist = self.reverse(left) + self.reverse(right)
        nums[:] = self.reverse(reverselist)       
        
    def reverse(self,nums):
        left ,right = 0, len(nums) - 1
        while left < right:
            nums[left] , nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums