# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A== None:
            return B
        elif B==None:
            return A
        if A.val <=B.val:
            C = A
            A =A.next
        else:
            C =B
            B= B.next
            
        curC =C
        while A != None and B != None :
            if A.val <=B.val:
                curC.next =A
                A =A.next
                curC=curC.next
            else:
                curC.next = B
                B =B.next
                curC =curC.next
        while A!=None:
            curC.next = A
            A=A.next
            curC= curC.next
        while B!= None:
            curC.next = B
            B=B.next
            curC =curC.next
            
        return C
                
