**Binary Tree - Depth First Search - Easy**

**Leaf-Similar Trees**

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence. For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8). Two binary trees are considered leaf-similar if their leaf value sequence is the same.Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

**Example 1:**
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

**Example 2:**
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

**Constraints:**
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

**Solution:**

- have an internal function for dfs
- the dfs function returns an empty array if there is no root node
- else it checks if the node has any leaves, it there aren't any children on the left or rights sides then it yields the value of the root
- the process is repeated recursively for the left and right sides of the tree and the values are yielded
- the purpose of yield is to return on-fly,as a part of a **generator**, an allows **lazy-evaluation** -- each value is generated and returned to the caller one at a time, when needed; the function does not have to finish the entire traversal to start returning values; which in turn gives rise to more efficient memory usage and cleaner code
- you could elimincate the use of yield by passing a list of integers to collect the leaves to the dfs function

**Time complexity- O(n1+n2)
Space Complexity- O(n1+n2)**
