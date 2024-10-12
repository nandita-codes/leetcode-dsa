# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node:TreeNode, max_val:int):
            if not node:
                return 
            nonlocal good_count
            if max_val<=node.val:
                good_count+=1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        good_count = 0
        dfs(root, float('-inf'))
        return good_count
