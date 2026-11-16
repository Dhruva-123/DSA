class Solution:
    def reverseLL(self, head):
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

    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        temp = head
        for _ in range((length - 1) // 2):
            temp = temp.next
        rightHalf = temp.next
        temp.next = None
        rightHalf = self.reverseLL(rightHalf)
        leftHalf = head
        while rightHalf:
            leftNext = leftHalf.next
            rightNext = rightHalf.next
            leftHalf.next = rightHalf
            rightHalf.next = leftNext
            leftHalf = leftNext
            rightHalf = rightNext