# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None

            # 我就是相信dfs會給我invert好的子樹
            left = dfs(root.left)
            right = dfs(root.right)

            root.left, root.right = right, left
            return root

        return dfs(root)
        