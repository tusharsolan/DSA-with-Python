# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        mid = self.getMid(head)
        left_head=head
        right_head = mid.next

        #broke the relation b/w two LL
        mid.next = None

        # Step 2: Sort both halves
        left_sorted_head = self.sortList(left_head)
        right_sorted_head = self.sortList(right_head)

        # Step 3: Merge both halves
        return self.merge(left_sorted_head, right_sorted_head)

    # Helper function to find the middle node
    def getMid(self, head):
        slow = head
        fast = head.next # we want first  middle ie m1 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper function to merge two sorted lists
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next