# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return None
        
        odd_pointer = head
        even_pointer = head.next

        evenHead = head.next
        while even_pointer and even_pointer.next:
            odd_pointer.next = odd_pointer.next.next
            odd_pointer = odd_pointer.next
            even_pointer.next = even_pointer.next.next
            even_pointer = even_pointer.next
        odd_pointer.next = evenHead
    
        return head
