# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, left_length:int, right_length:int):
            if not node:
                return 0
            nonlocal max_zigzag
            max_zigzag = max(max_zigzag, left_length, right_length)
            dfs(node.left, right_length+1, 0)
            dfs(node.right, 0, left_length+1)

            
        max_zigzag = 0
        dfs(root,0,0)
        return max_zigzag
