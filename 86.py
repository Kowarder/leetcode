# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        b_c, a_c = before, after
        while head:
            if head.val < x:
                b_c.next = head
                b_c = head
            else:
                a_c.next = head
                a_c = head
            head = head.next
        
        a_c.next = None
        b_c.next = after.next
        return before.next
