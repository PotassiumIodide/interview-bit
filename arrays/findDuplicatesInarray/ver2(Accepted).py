class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        for i in range(len(A)):
            if(A[abs(A[i])] >= 0):
                A[abs(A[i])] = -A[abs(A[i])]
            else:
                return abs(A[i])
