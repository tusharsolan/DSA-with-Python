# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #if only 1 list is there then no intersection
        if headA == None or headB == None :
            return None
        #placing at heads    
        t1=headA
        t2=headB

        while t1!=t2 :
            t1=t1.next
            t2=t2.next

            #check if first element is equal
            if t1==t2 :
                return t1

            if t1 ==  None:

                #placing t1 to  2 nd list head ie headB
                t1=headB

            if t2 == None:


                #placing t2 to 1 st list head ie headA
                t2=headA

        #can return t1 or t2        
        return t1                    
        