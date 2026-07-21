# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and n==1:
            return None
        
        #reverse
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #remove nth node: node.next = node.next.next
        reversed_list = prev
        curr = prev
        if n == 1:
            reversed_list = reversed_list.next
        if n >= 2:
            for _ in range(n-2):
                curr = curr.next
        curr.next = curr.next.next

        #reverse it back
        curr = reversed_list
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
        