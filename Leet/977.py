class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)- 1
        sorted = []
        
        while left <= right:
            
            numLeft = nums[left]
            numRight = nums[right]
            # right is bigger
            if (numLeft)**2 < (numRight)**2:
                sorted.insert(0,numRight ** 2)
                right -= 1
            # same or left is bigger
            else :
                sorted.insert(0,numLeft ** 2)
                left += 1
        
        return sorted
            