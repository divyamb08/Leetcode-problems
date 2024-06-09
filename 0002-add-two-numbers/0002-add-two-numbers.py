# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        cur1 = l1
        cur2 = l2
        rem = 0
        dummy = ListNode(0)
        dummyhead = dummy
        dummycur = dummy
        while cur1 and cur2:
            value = cur1.val + cur2.val + rem
            if value>9:
                rem = 1
            else: rem = 0
            new = ListNode(value%10)
            dummycur.next = new
            cur1, cur2, dummycur = cur1.next, cur2.next, dummycur.next
        
        while cur1:
            value = rem + cur1.val
            if value>9:rem=1 
            else: rem=0
            dummycur.next = ListNode(value%10)
            cur1 = cur1.next
            dummycur = dummycur.next
            
        while cur2:
            value = rem + cur2.val
            if value>9:rem=1 
            else: rem=0
            dummycur.next = ListNode(value%10)
            cur2 = cur2.next
            dummycur = dummycur.next
        
        if rem == 1:
            dummycur.next = ListNode(1)
            dummycur = dummycur.next
            
        return dummyhead.next
            
            
            