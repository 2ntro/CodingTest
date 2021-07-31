class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,value in enumerate(numbers,start=0):
            remaining = target- numbers[i]
            if remaining in seen:
                return [seen[remaining]+1,i+1]
            else:
                seen[value] = i

sol = Solution()

numbers =[2,7,11,15]
target = 9
print(sol.twoSum(numbers,target))