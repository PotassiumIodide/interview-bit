# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        C=A
        length =0
        while C!=None:
            length+=1
            C=C.next
            
        if B > length:
            return A.next
            
        count =0
        C=A
        prev =None
        
        while count <length:
            count+=1
            if B ==length:
                return A.next
            if count !=length-B+1:
                prev =C
                C =C.next
            else:
                prev.next =C.next
                return A
                
                
                
                
                
