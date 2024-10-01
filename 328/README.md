**Linked List -- Medium - **

**Problem:**

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

**Example 2:**
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

**Constraints:**
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6


**Solution:**
- Link all the odd pointers by using 'odd_pointer.next = odd_pointer.next.next ==> odd_pointer = odd_pointer.next'
- Follow the same for the even nodes --> 'even_pointer.next = even_pointer.next.next ==> even_pointer = even_pointer.next'
- Finally have another pointer 'evenHead' to keep track of the start point of the even nodes linking
- Link the last node of the odd_pointer to the evenHead
