# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #temp=head
        fast=head
        for i in range(n):
            fast=fast.next
            
        # If fast is None, we are deleting the head
        if fast == None:
            return head.next    

        slow=head

        # Move both until fast reaches end
        while fast.next :
            slow=slow.next
            fast=fast.next
        

        # Delete the node
        slow.next=slow.next.next  

        return head              

        