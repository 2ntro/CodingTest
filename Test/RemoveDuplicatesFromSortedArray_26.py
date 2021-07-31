class Solution(object):
    def removeDuplicates(self, nums:list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre:int = None
        for i,num in enumerate(nums):

            if pre == num:
                nums.pop(pre)
            pre = num
        else:
            return(len(nums))
sol = Solution()
nums =[0,0,1,1,1,2,2,3,3,4]

print(sol.removeDuplicates(nums))
print(nums)