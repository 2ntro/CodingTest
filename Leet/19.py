# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        
        
        length = 1
        # loop 가 끝나면 slow는 중간 fast는 끝
        while fast and fast.next:

            fast = fast.next
            length += 1
            
        # target이 distance 만큼 멀리 있음
        distance = length - n
        # 출발
        before = head
        
        if distance != 0:
            # before 접근
            distance -= 1
            while distance:
                before = before.next
                distance -= 1
        target = before.next
        before.next = None    
        if target:
            if target.next:
                before.next = target.next
        else:
            head = None
        return head