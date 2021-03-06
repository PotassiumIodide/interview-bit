# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        s= set()
        C =A
        while C != None:
            if C in s:
                return C
                break
            else:
                s.add(C)
                C=C.next
        return None
                
