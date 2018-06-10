class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n =len(A)
        # Add 1 to last digit and find carry
        A[n-1] =A[n-1]+1
        carry = A[n-1]//10
        A[n-1]= A[n-1]%10
        # Traverse from second last digit
        for i in range(n-2,-1,-1):
            if carry ==1:
                A[i] =A[i]+1
                carry = A[i]//10
                A[i] =A[i]%10
        # If carry is 1, we need to add
        # a 1 at the beginning of vector
        if carry == 1:
            A.insert(0,1)
        
        for j in range(0,len(A)):
            if A[j]!=0:
                break
        n = len(A)
        newn = n-j
        return A[j:newn+j]
