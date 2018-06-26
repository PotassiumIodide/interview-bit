# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        C=A
        length=0        #Find Length of List
        while C!=None:
            length+=1
            C=C.next
            
        B=B%length       #In case B is greater than length of list 
        if B==0:
            return A
            
        C= A  
        k=length-B-1
        while k!=0:
            C=C.next
            k-=1
        new =C.next      #New is the pointer of element that will be at head
        C.next =None
        end =new
        while end.next!=None:
            end =end.next
        end.next  =A
        
        return new
        
