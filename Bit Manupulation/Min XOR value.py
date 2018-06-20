class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        minimum = 2**31 -1
        A =list(sorted(A))
        for i in range(len(A)-1):
            if A[i]^A[i+1]<minimum:
                minimum = A[i]^A[i+1]
        return minimum
            
