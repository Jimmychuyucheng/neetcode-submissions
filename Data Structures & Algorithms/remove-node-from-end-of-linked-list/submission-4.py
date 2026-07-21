# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 輔助函式：反轉鏈結串列
        def reverse(node):
            prev = None
            while node:
                node.next, prev, node = prev, node, node.next
            return prev

        # 1. 第一次反轉
        rev_head = reverse(head)
        
        # 2. 引入 dummy node 統整刪除邏輯
        dummy = ListNode(0, rev_head)
        curr = dummy
        
        # 往後走 n-1 步，剛好停在要被刪除節點的前一個
        for _ in range(n - 1):
            curr = curr.next
            
        # 執行刪除
        curr.next = curr.next.next
        
        # 3. 第二次反轉回來並回傳
        return reverse(dummy.next)