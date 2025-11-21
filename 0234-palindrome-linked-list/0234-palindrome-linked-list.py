# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse_linked_list(self, head):
        prev = None
        curr = head
        
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        
        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # Find middle using slow & fast pointers
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = self.reverse_linked_list(slow.next)

        # Compare both halves
        first = head
        temp = second  # store to restore later
        while second:
            if first.val != second.val:
                # Restore original list
                self.reverse_linked_list(temp)
                return False
            first = first.next
            second = second.next

        # Restore original list
        self.reverse_linked_list(temp)

        return True
