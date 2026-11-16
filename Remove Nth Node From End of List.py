class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length == n:
            return head.next
        prev = head
        for i in range(length - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head