# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # 1. find the medium and split into two pieces by slow fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next = None
        
        # 2. reverse the second half pieces
        rev_sec = None
        curr = sec
        while curr:
            tmp = curr.next
            curr.next = rev_sec
            rev_sec = curr
            curr = tmp
        
        
        # 3. merge two peices in an order
        first = head
        sec = rev_sec
        res = ListNode(0)
        curr = res
        while first and sec:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = sec
            sec = sec.next
            curr = curr.next

        if first:
            curr.next = first

        if sec:
            curr.next = sec



