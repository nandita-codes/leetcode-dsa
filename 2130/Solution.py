# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev    

        ans =0
        slow, fast= head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = reverseList(slow)

        while tail:
            ans = max(ans, head.val+tail.val)
            head = head.next
            tail = tail.next
        
        return ans
