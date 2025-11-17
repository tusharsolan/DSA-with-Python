# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # Initialize the slow pointer to the head.
        slow = head   
    
        # Initialize the fast pointer to the head.
        fast = head   

        # Traverse the linked list using
        # the Tortoise and Hare algorithm.
        while fast and fast.next :
            # Move fast two steps.
            fast = fast.next.next 
            # Move slow one step.
            slow = slow.next       

        # Return the slow pointer,
        # which is now at the middle node.
        return slow  
        