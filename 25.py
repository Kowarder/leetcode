# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def solve(head, k, size):
            if size < k:
                return head
            if head is None:
                return None
            cur = head
            nn = None
            prev = None
            ct = 0
            while cur is not None and ct < k:
                nn = cur.next
                cur.next = prev
                prev = cur
                cur = nn
                ct += 1
            head.next = solve(nn, k, size-k)
            return prev
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        return solve(head, k, length)
