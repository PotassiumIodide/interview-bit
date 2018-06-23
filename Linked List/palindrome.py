class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        stack = []
        
        while A:
            stack.append(A.val)
            A = A.next
            
        if stack == list(reversed(stack)):
            return 1
        else:
            return 0
