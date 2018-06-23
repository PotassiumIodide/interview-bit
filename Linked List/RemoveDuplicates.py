# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        C =A
        curC =C
        while A!= None and A.next!=None:
            if A.val == A.next.val:
                A =A.next
            else:
                curC.next =A.next
                A =A.next
                curC= curC.next
        curC.next=None
        
        return C
