class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # find the middle of the list by slow, fast pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        #split the two list
        slow.next = None

        #reversed the second list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp

        #merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        


        