# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize 'temp' at the
        # head of the linked list
        temp=head
        # Initialize 'prev' to None,
        # representing the previous node 
        prev=None

        while temp:
            # Store the next node in 'front'
            # to preserve the reference
            front=temp.next
            # Reverse the direction of the current
            # node's 'next' pointer to point to 'prev'
            temp.next=prev
            # Move 'prev' to the current 
            # node, for the next iteration
            prev=temp
            # Move 'temp' to 'front' node
            # advancing traversal
            temp=front

        # Return the new head
        # of the reversed linked list
        return prev
        