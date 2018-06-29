# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        listdic ={}
        newhead = RandomListNode(head.label)
        A = head
        listdic[head] =newhead
        B =newhead
        A =A.next
        while A!=None:
            temp =RandomListNode(A.label)
            B.next  =temp
            listdic[A] =temp
            A=A.next
            B= B.next
        
        
        A= head
        B=newhead
        while A!=None:
            B.random =listdic.get(A.random)
            A=A.next
            B= B.next
        
        return newhead
            
        
