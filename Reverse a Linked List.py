# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        anchor = head.next
        current = head
        prev = None
        while current:
            current.next = prev
            prev = current
            current = anchor
            if anchor:
                anchor = anchor.next
        return prev
