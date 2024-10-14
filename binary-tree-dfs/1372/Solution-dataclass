from dataclasses import dataclass
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
@dataclass (frozen=True)
class T:
    leftMax:int
    rightMax:int
    subtreeMax:int

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode)->T:
            if not node:
                return T(-1,-1,-1)
            left = dfs(node.left)
            right = dfs(node.right)
            left_zigzag = left.rightMax+1
            right_zigzag = right.leftMax+1
            subtreeMax = max(left_zigzag, right_zigzag, left.subtreeMax, right.subtreeMax)

            return T(left_zigzag, right_zigzag, subtreeMax)
        
        return dfs(root).subtreeMax
