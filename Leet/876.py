# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nexthead(self,head):
        return head.next
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        secondhead = head
        length = 0
        while secondhead:
            secondhead = secondhead.next
            length += 1
        left = 0
        right = length - 1
        
        while left < right :
            left += 1
            right -= 1
        result = []
        for _ in range(length):
            if _ >= left:
                return head
                
            head = head.next
