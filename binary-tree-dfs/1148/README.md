**Binary Tree - DFS - Medium**
**Count Good Nodes in Binary Tree**

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

**Example 1:**

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

**Example 2:**
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

**Example 3:**
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

**Constraints:**
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

**Solution:**
- Have a function dfs that iterates through the nodes to see if and compare the value of the nodes with a parameter 'max_val'
- If node.val is greater than max_val, increase the good_node_count by one and change the max_val to node.val
- Do this recursively for the left and right sides of the tree
- Use 'nonlocal' inside the dfs function to declare the good_node_count and update that whenever necessary; this ensures that the global variable is updated
- Return the value of good_node_count from the outer function after invoking dfs for the root node

**Time Complexity-O(n)
Space Complexity-O(logn) best case-balanced tree, O(n) worst case-unbalanced tree**
