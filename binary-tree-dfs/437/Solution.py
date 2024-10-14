from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node:Optional[TreeNode], curr_sum:int):
            if not node:
                return 0
            curr_sum += node.val
            path_count = paths_count[curr_sum-targetSum]
            paths_count[curr_sum]+=1
            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)
            paths_count[curr_sum]-=1
            return path_count
        
        paths_count = Counter({0:1})
        return dfs(root, 0)
