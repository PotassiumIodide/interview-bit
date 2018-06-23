# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        repeat =False
        ini =None
        C=None
        curC=None
        if A== None :
            return A
        if A.next ==None:
            return A
        while A!= None and A.next!=None:
            if A.val == A.next.val:
                A =A.next
                repeat =True
            else:
                if repeat:
                    A=A.next
                    repeat =False
                else:
                    if ini==None:
                        C=A
                        curC=C
                        ini=1
                        A=A.next
                    else:
                        curC.next =A
                        A =A.next
                        curC =curC.next
        if curC != None:
            if repeat==False:
                curC.next =A
                curC =curC.next
                curC.next= None
            else:
                curC.next= None
        
        return C
