# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If list has only one node, delete it
        if head == None or head.next == None:
            return None

        slow=fast=head

        # Initialize fast pointer two steps ahead or skip the slow for 1 time
        fast=fast.next.next

        # Traverse until fast reaches end
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # Bypass the middle node
        slow.next=slow.next.next

        # Return head of updated list
        return head        
        