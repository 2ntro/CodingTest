# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        print(id(dummy))
        
        First = dummy
        Second = dummy
        print(id(First))
        First_distance = n + 1
        while First_distance > 0:
            First_distance -= 1
            First = First.next
        while First != None:
            First = First.next
            Second = Second.next
        Second.next = Second.next.next
        return dummy.next