# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev



# 0->1->2->3

# prev = null head=0: tmp = 1 head.next=null prev=0 head = 1
# prev = 0 head = 1: tmp = 2 head.next=0 prev=1 head=2. null<-0<-1



        