
def isBadVersion(pivot):
        target = 4
        if pivot >= target:
            return True
        else:
            return False

class Solution(object):
    
    def firstBadVersion(self, n):
        left , right = 1, n
        
        while left <= right:
            pivot = left + (right - left) // 2
           
            # is G
            if isBadVersion(pivot) == False:
                left = pivot + 1
            # is B
            elif isBadVersion(pivot) == True:
                right = pivot - 1
        return left