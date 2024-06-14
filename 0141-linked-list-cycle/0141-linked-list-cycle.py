# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        temp = head
        while temp:
            if id(temp) in d:
                return True
            d[id(temp)] = 1
            temp = temp.next
        return False