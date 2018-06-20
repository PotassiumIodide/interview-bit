class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n =len(A)
        if len(A)==0:
            return len(A)
        
        k =0
        for i in range(len(A)-1):
            if A[i+1]!= A[i]:
                A[k]=A[i]
                k+=1
        A[k]=A[n-1]
        k+=1
        return k
        
