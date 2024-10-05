**Binary Tree - Depth First Search -- Easy**

**Maximum Depth of Binary Tree**

**Example 1:**
Input: root = [3,9,20,null,null,15,7]
Output: 3

**Example 2:**
Input: root = [1,null,2]
Output: 2

**Constraints:**
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100

**Solution:**
- If not root, return 0 -- this essentially returns 0 if there is no child existing -- that is, no node could be passed as a root
- Otherwise, return 1 + (maximum of the left and right branches)

**Time Complexity- O(n) -- Each node is visited once to calculate depth
Space Complexity- O(n) -- in the worst case; O(logn) in the best case**
