# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if A == None :
            return B
        elif B == None :
            return A
        carry = 0
        res =0
        
        while A != None and B!= None:
            temp = A.val+B.val+carry
            carry  =temp//10
            newnode =ListNode(0)
            newnode.next=None
            newnode.val =temp%10
            if res == 0:
                res = newnode
                cur = res
            else:
                cur.next =newnode
                cur =cur.next
            A =A.next 
            B=B.next
                
        while A!= None:
            temp  =A.val+carry
            carry = temp//10
            newnode =ListNode(0)
            newnode.next = None
            newnode.val =temp%10
            cur.next =newnode
            cur =cur.next
            A =A.next
            
        while B!= None:
            temp  =B.val+carry
            carry = temp//10
            newnode =ListNode(0)
            newnode.next = None
            newnode.val=temp%10
            cur.next =newnode
            cur =cur.next
            B =B.next
            
        if carry == 1:
            newnode = ListNode(0)
            newnode.next = None
            newnode.val = carry
            cur.next = newnode
            cur = cur.next
        return res
