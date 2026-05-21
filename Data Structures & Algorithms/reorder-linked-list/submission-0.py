class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 步驟一：用快慢指標找到中點，把鏈表切成兩半
        slow, fast = head, head
        while fast and fast.next: # 這就是你剛學會的防錯神招！
            slow = slow.next
            fast = fast.next.next
            
        # 此時 slow 就是中點。我們把後半段拆出來
        mid = slow.next
        slow.next = None # 正式把前半段的尾巴斷開，切成兩條獨立鏈表
        
        # 步驟二：翻轉後半段鏈表 (mid)
        prev = None
        curr = mid
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        reversed_list = prev # 這條是翻轉後的後半段頭

        # 步驟三：交錯合併兩條鏈表 (head 和 reversed_list)
        first = head
        second = reversed_list
        while second: # 因為後半段一定比較短或一樣長，以它為基準判斷即可
            # 先把兩邊的「下一步」存起來，免得斷開後找不到
            tmp1 = first.next
            tmp2 = second.next
            
            # 開始交叉連接
            first.next = second  # 前半段接後半段
            second.next = tmp1   # 後半段接原本前半段的下一個
            
            # 指標往前推進，繼續下一輪交織
            first = tmp1
            second = tmp2