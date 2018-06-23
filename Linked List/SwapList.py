# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        temp=A
        while temp !=None and temp.next!= None:
            C =temp.next.val
            temp.next.val =temp.val
            temp.val =C
            temp = temp.next.next
        return A
        
        
