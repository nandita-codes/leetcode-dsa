**Linked List - Easy**

Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


**Example 2:**
Input: head = [1,2]
Output: [2,1]

**Constraints:**
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


**Solution:**

**Iterative-**
- Have a node 'prev' thar is None -- has no value and points to null, and have a node 'curr' that points to the 'head'
- Iterate while curr exists -- make next point to curr.next
- Make curr.next as prev
- Shift prev to curr
- Shift curr to next
- Return the 'prev' pointer at the end of the function
  
**Time Complexity - O(n)
Space Complexity - O(1)**

**Recursive-**
- If 'head' or 'head.next' does not exist, return head -- which would essentially be null
- If the loop doesn't end there, initialize newHead as self.reverseList(head.next) -- this makes the head recursively return the required node
- Make head.next.next point to head, this is the step that reverses the list
- To make sure that there isn't a cycle, make head.next as None
- Return newHead -- this is what gets returned to the recursive step

**Time Complexity - O(n)
Space Complexity - O(n) -- since we have the 'newHead' pointer -- recursive stack**


